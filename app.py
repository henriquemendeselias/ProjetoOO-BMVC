# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from app.models.jogador import Jogador
from app.db.persistencia_jogador import PersistenciaJogador
from app.models.posicao import Posicao
from app.db.persistencia_posicao import PersistenciaPosicao

app = Flask(__name__, 
            template_folder='app/html',
            static_folder='app/static')

db = PersistenciaJogador()
db_pos = PersistenciaPosicao()

@app.route('/')
@app.route('/index')
def action_index():
    """
    Read do Crud - ler todos
    """
    jogadores_lista = db.listar_todos()
    posicoes_lista = db_pos.listar_todos()
    posicoes_map = {pos.get_id(): pos.get_nome() for pos in posicoes_lista}
    return render_template('index.tpl', jogadores=jogadores_lista, posicoes_map=posicoes_map)

@app.route('/formulario', methods=['GET', 'POST'])
def action_formulario_novo():
    """
    Create do CRUD - GET e POST
    Mostra o formulário vazio - get
    Recebe os dados e salva - post
    """
    if request.method == 'POST':
        nome = request.form.get('nome')
        posicao_id = request.form.get('posicao_id')
        numero = request.form.get('numero_camisa')
        novo_jogador = Jogador(nome=nome, posicao_id=posicao_id, numero_camisa=numero)
        db.salvar(novo_jogador)
        return redirect(url_for('action_index'))
    
    jogador_vazio = {
        "id": "",
        "nome": "",
        "posicao_id": "",
        "numero_camisa": ""
    }
    
    lista_posicoes = db_pos.listar_todos()

    contexto = {
        "jogador": jogador_vazio,
        "titulo_pagina": "Novo Jogador",
        "titulo_h2": "Cadastrar Novo Jogador",
        "url_destino": url_for('action_formulario_novo'),
        "lista_posicoes": lista_posicoes
    }
    
    return render_template('forms_jogador.tpl', **contexto)

@app.route('/editar/<jogador_id>', methods=['GET'])
def action_formulario_editar(jogador_id):
    """
    Update do CRUD - get
    """
    jogador = db.buscar_por_id(jogador_id)
    if not jogador:
        return redirect(url_for('action_index'))
    
    lista_posicoes = db_pos.listar_todos()

    contexto = {
        "jogador": jogador,
        "titulo_pagina": "Editar Jogador",
        "titulo_h2": f"Editando: {jogador.get_nome()}",
        "url_destino": url_for('action_salvar_edicao'),
        "lista_posicoes": lista_posicoes 
    }
    
    return render_template('forms_jogador.tpl', **contexto)

@app.route('/editar/salvar', methods=['POST'])
def action_salvar_edicao():
    """
    Update do CRUD - post
    """
    id_jogador = request.form.get('id')
    nome = request.form.get('nome')
    posicao_id = request.form.get('posicao_id')
    numero = request.form.get('numero_camisa')

    jogador_atualizado = Jogador(nome=nome, posicao_id=posicao_id, numero_camisa=numero, id=id_jogador)
    
    db.atualizar(jogador_atualizado)
    
    return redirect(url_for('action_index'))

@app.route('/deletar/<jogador_id>', methods=['GET'])
def action_deletar(jogador_id):
    """
    Delet do CRUD - get
    """
    db.deletar(jogador_id)

    return redirect(url_for('action_index'))

@app.route('/posicoes')
def action_posicoes_index():
    """
    Mostra a lista de todas as posições cadastradas
    """
    lista_de_posicoes = db_pos.listar_todos()
    return render_template('posicao_index.tpl', posicoes=lista_de_posicoes)

@app.route('/posicao/nova', methods=['GET', 'POST'])
def action_posicao_nova():
    """
    Create do CRUD - GET e POST
    Mostra o formulário vazio - get
    Recebe os dados, cria o objeto e salva - post
    """
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        sigla = request.form.get('sigla')
        
        nova_posicao = Posicao(nome=nome, sigla=sigla)
        db_pos.salvar(nova_posicao)
        
        return redirect(url_for('action_posicoes_index'))

    posicao_vazia = {"id": "", "nome": "", "sigla": ""}
    contexto = {
        "posicao": posicao_vazia,
        "titulo_pagina": "Nova Posição",
        "titulo_h2": "Cadastrar Nova Posição",
        "url_destino": url_for('action_posicao_nova')
    }
    return render_template('forms_posicao.tpl', **contexto)

@app.route('/posicao/editar/<posicao_id>', methods=['GET', 'POST'])
def action_posicao_editar(posicao_id):
    """
    Uptade do CRUD - get e post
    Busca a posição pelo ID e mostra o formulario, permitindo e edição - get
    Recebe os dados, atualiza o objeto e salva - post
    """

    if request.method == 'POST':
        id_pos = request.form.get('id') 
        nome = request.form.get('nome')
        sigla = request.form.get('sigla')
        
        posicao_atualizada = Posicao(nome=nome, sigla=sigla, id=id_pos)
        db_pos.atualizar(posicao_atualizada)
        
        return redirect(url_for('action_posicoes_index'))

    posicao = db_pos.buscar_por_id(posicao_id)
    if not posicao:
        return redirect(url_for('action_posicoes_index'))

    contexto = {
        "posicao": posicao,
        "titulo_pagina": "Editar Posição",
        "titulo_h2": f"Editando: {posicao.get_nome()}",
        "url_destino": url_for('action_posicao_editar', posicao_id=posicao.get_id())
    }
    return render_template('forms_posicao.tpl', **contexto)

@app.route('/posicao/deletar/<posicao_id>')
def action_posicao_deletar(posicao_id):
    """
    Delet do CRUD
    """
    db_pos.deletar(posicao_id)
    return redirect(url_for('action_posicoes_index'))

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
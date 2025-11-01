# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for

from app.models.jogador import Jogador
from app.models.posicao import Posicao
from app.models.time import Time

from app.db.persistencia_jogador import PersistenciaJogador
from app.db.persistencia_posicao import PersistenciaPosicao
from app.db.persistencia_time import PersistenciaTime

app = Flask(__name__, 
            template_folder='app/html',
            static_folder='app/static')

db = PersistenciaJogador()
db_pos = PersistenciaPosicao()
db_time = PersistenciaTime()

@app.route('/')
@app.route('/times')
def action_times_index():
    lista_de_times = db_time.listar_todos()
    return render_template('time_index.tpl', times=lista_de_times)

@app.route('/elenco/<time_id>')
def action_elenco_detalhes(time_id):

    jogadores_lista_completa = db.listar_todos()
    jogadores_filtrados = [j for j in jogadores_lista_completa if j.get_time_id() == time_id]

    posicoes_lista = db_pos.listar_todos()
    posicoes_map = {pos.get_id(): pos.get_nome() for pos in posicoes_lista}

    time_obj = db_time.buscar_por_id(time_id)
    if not time_obj:
        return redirect(url_for('action_times_index'))

    return render_template('index.tpl', jogadores=jogadores_filtrados, posicoes_map=posicoes_map, time=time_obj)

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
        time_id = request.form.get('time_id')
        numero = request.form.get('numero_camisa')
        data_nasc = request.form.get('data_nascimento')
        nacionalidade = request.form.get('nacionalidade')

        novo_jogador = Jogador(nome=nome, posicao_id=posicao_id, time_id=time_id, numero_camisa=numero, data_nascimento=data_nasc, nacionalidade=nacionalidade)

        db.salvar(novo_jogador)

        return redirect(url_for('action_elenco_detalhes', time_id=time_id))
    
    time_preselecionado_id = request.args.get('time_id', None)
    time_obj = None
    if time_preselecionado_id:
        time_obj = db_time.buscar_por_id(time_preselecionado_id)
    
    jogador_vazio = {
        "id": "",
        "nome": "",
        "posicao_id": "",
        "time_id":time_preselecionado_id,
        "numero_camisa": "",
        "data_nascimento": "",
        "nacionalidade": ""
    }
    
    lista_posicoes = db_pos.listar_todos()
    lista_times = db_time.listar_todos()

    contexto = {
        "jogador": jogador_vazio,
        "time": time_obj,
        "titulo_pagina": "Novo Jogador",
        "titulo_h2": "Cadastrar Novo Jogador",
        "url_destino": url_for('action_formulario_novo'),
        "lista_posicoes": lista_posicoes,
        "lista_times": lista_times
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
    lista_times = db_time.listar_todos()

    contexto = {
        "jogador": jogador,
        "titulo_pagina": "Editar Jogador",
        "titulo_h2": f"Editando: {jogador.get_nome()}",
        "url_destino": url_for('action_salvar_edicao'),
        "lista_posicoes": lista_posicoes,
        "lista_times": lista_times
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
    time_id = request.form.get('time_id')
    numero = request.form.get('numero_camisa')
    data_nasc = request.form.get('data_nascimento')
    nacionalidade = request.form.get('nacionalidade')

    jogador_atualizado = Jogador(nome=nome, posicao_id=posicao_id, time_id=time_id, numero_camisa=numero, data_nascimento=data_nasc, nacionalidade=nacionalidade, id=id_jogador)
    
    db.atualizar(jogador_atualizado)
    
    return redirect(url_for('action_elenco_detalhes', time_id=time_id))

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

@app.route('/time/novo', methods=['GET', 'POST'])
def action_time_novo():
    """
    Create do CRUD - get e post
    Mostra o formulario - get
    Recebe os dados, cria o objeto Time e salva - post
    """

    if request.method == 'POST':
        nome = request.form.get('nome')
        tipo = request.form.get('tipo')
        
        novo_time = Time(nome=nome, tipo=tipo)
        db_time.salvar(novo_time)
        
        return redirect(url_for('action_times_index'))
    
    time_vazio = {"id": "", "nome": "", "tipo": ""}
    contexto = {
        "time": time_vazio,
        "titulo_pagina": "Novo Elenco",
        "titulo_h2": "Cadastrar Novo Elenco",
        "url_destino": url_for('action_time_novo')
    }
    return render_template('forms_time.tpl', **contexto)

@app.route('/time/editar/<time_id>', methods=['GET', 'POST'])
def action_time_editar(time_id):
    """
    Update do CRUD - get e post
    Busca o Time por ID e mostra o formulario, permitindo edição - get
    Recebe os dados, atualiza o objeto Time e salva - post
    """

    if request.method == 'POST':
        id_time = request.form.get('id') 
        nome = request.form.get('nome')
        tipo = request.form.get('tipo')
        
        time_atualizado = Time(nome=nome, tipo=tipo, id=id_time)
        db_time.atualizar(time_atualizado)
        
        return redirect(url_for('action_times_index'))

    time = db_time.buscar_por_id(time_id)
    if not time:
        return redirect(url_for('action_times_index'))

    contexto = {
        "time": time,
        "titulo_pagina": "Editar Elenco",
        "titulo_h2": f"Editando: {time.get_nome()}",
        "url_destino": url_for('action_time_editar', time_id=time.get_id())
    }
    return render_template('forms_time.tpl', **contexto)

@app.route('/time/deletar/<time_id>')
def action_time_deletar(time_id):
    """
    Delet do CRUD - deleta um time e volta para a lista
    """
    db_time.deletar(time_id)
    return redirect(url_for('action_times_index'))

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
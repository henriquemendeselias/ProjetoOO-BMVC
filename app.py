# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from app.models.jogador import Jogador
from app.db.persistencia_jogador import PersistenciaJogador

app = Flask(__name__, 
            template_folder='app/html',
            static_folder='app/static')

db = PersistenciaJogador()

@app.route('/')
@app.route('/index')
def action_index():
    """
    Read do Crud - ler todos
    """
    jogadores_lista = db.listar_todos()
    return render_template('index.tpl', jogadores=jogadores_lista)

@app.route('/formulario', methods=['GET', 'POST'])
def action_formulario_novo():
    """
    Create do CRUD - GET e POST
    Mostra o formulário vazio - get
    Recebe os dados e salva - post
    """
    if request.method == 'POST':
        nome = request.form.get('nome')
        posicao = request.form.get('posicao')
        numero = request.form.get('numero_camisa')
        novo_jogador = Jogador(nome=nome, posicao=posicao, numero_camisa=numero)
        db.salvar(novo_jogador)
        return redirect(url_for('action_index'))
    
    jogador_vazio = {
        "id": "",
        "nome": "",
        "posicao": "",
        "numero_camisa": ""
    }
    
    contexto = {
        "jogador": jogador_vazio,
        "titulo_pagina": "Novo Jogador",
        "titulo_h2": "Cadastrar Novo Jogador",
        "url_destino": url_for('action_formulario_novo')
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
    contexto = {
        "jogador": jogador,
        "titulo_pagina": "Editar Jogador",
        "titulo_h2": f"Editando: {jogador.get_nome()}",
        "url_destino": url_for('action_salvar_edicao') 
    }
    
    return render_template('forms_jogador.tpl', **contexto)

@app.route('/editar/salvar', methods=['POST'])
def action_salvar_edicao():
    """
    Update do CRUD - post
    """
    id_jogador = request.form.get('id')
    nome = request.form.get('nome')
    posicao = request.form.get('posicao')
    numero = request.form.get('numero_camisa')

    jogador_atualizado = Jogador(nome=nome, posicao=posicao, numero_camisa=numero, id=id_jogador)
    
    db.atualizar(jogador_atualizado)
    
    return redirect(url_for('action_index'))

@app.route('/deletar/<jogador_id>', methods=['GET'])
def action_deletar(jogador_id):
    """
    Delete do CRUD - get
    """
    db.deletar(jogador_id)

    return redirect(url_for('action_index'))

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
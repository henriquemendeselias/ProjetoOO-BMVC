from bottle import template, request, redirect
from app.models.jogador import Jogador
from app.controllers.db.persistencia_jogador import PersistenciaJogador

class Application():

    def __init__(self):
        self.db = PersistenciaJogador()

    def helper(self):
        return template('app/html/helper')

    def index(self):
        """
        Read do CRUD - ler todos
        """
        jogadores_lista = self.db.listar_todos()
        return template('app/html/index', jogadores = jogadores_lista)
    
    def formulario_novo(self):
        """
        Create do CRUD - só exibe o forms - get
        """
        dados_jogador = {
            "id": "",
            "nome": "",
            "posicao": "",
            "numero_camisa": "",
            "titulo_pagina": "Novo Jogador",
            "titulo_h2": "Cadastrar Novo Jogador",
            "url_destino": "/formulario/salvar"
        }

        return template('app/html/forms_jogador', **dados_jogador)
    
    def salvar_novo(self):
        """
        Create do CRUD - recebe os dados de forms e salva o novo jogador - post
        """
        nome = request.forms.get('nome')
        posicao = request.forms.get('posicao')
        numero = request.forms.get('numero_camisa')

        novo_jogador = Jogador(nome=nome, posicao=posicao, numero_camisa=numero)
        
        self.db.salvar(novo_jogador)
        
        return redirect('/')
    
    def formulario_editar(self, jogador_id):
        """
        Update do CRUD (get) - busca por id e mostra o forms preenchifo, permitindo edição.
        """
        jogador = self.db.buscar_por_id(jogador_id)
        
        if not jogador:
            return redirect('/')

        dados_jogador = {
            "id": jogador.get_id(),
            "nome": jogador.get_nome(),
            "posicao": jogador.get_posicao(),
            "numero_camisa": jogador.get_numero_camisa(),
            "titulo_pagina": "Editar Jogador",
            "titulo_h2": f"Editando: {jogador.get_nome()}",
            "url_destino": "/editar/salvar"
        }
        
        return template('app/html/forms_jogador', **dados_jogador)
    
    def salvar_edicao(self):
        """
        Update do CRUD (post) - recebe os dados do formulario de edição e atualiza o jogador.
        """
        id = request.forms.get('id')
        nome = request.forms.get('nome')
        posicao = request.forms.get('posicao')
        numero = request.forms.get('numero_camisa')

        jogador_atualizado = Jogador(nome=nome, posicao=posicao, numero_camisa=numero, id=id)
        
        self.db.atualizar(jogador_atualizado)
        
        return redirect('/')

    def deletar(self, jogador_id):
        """
        delete do crud (get) - recebe um ID e manda a persistência apagar o jogador.
        """

        self.db.deletar(jogador_id)
        
        return redirect('/')
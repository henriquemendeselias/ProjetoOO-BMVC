import json
import os
from app.models.jogador import Jogador

class PersistenciaJogador:

    FILE_PATH = os.path.join('app', 'db', 'elenco.json')

    def __init__(self):
        self._garantir_arquivo_existe()

    def _garantir_arquivo_existe(self):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)
        
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _ler_arquivo(self):
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return dados if isinstance(dados, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return [] 

    def _escrever_arquivo(self, dados):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def salvar(self, jogador):
        """
        Create do CRUD
        """
        dados = self._ler_arquivo()
        dados.append(jogador.to_dict()) 
        self._escrever_arquivo(dados)

    def listar_todos(self):
        """
        Read do CRUD - ler todos
        """
        dados = self._ler_arquivo()
        jogadores = [Jogador.from_dict(j) for j in dados]
        return jogadores

    def buscar_por_id(self, jogador_id):
        """
        Read do CRUD - ler um por um
        """
        dados = self._ler_arquivo()
        for jdict in dados:
            if jdict.get('id') == jogador_id:
                return Jogador.from_dict(jdict)
        return None

    def atualizar(self, jogador_atualizado):
        """
        Update do CRUD
        """
        dados = self._ler_arquivo()
        dados_atualizados = []
        encontrou = False
        for jdict in dados:
            if jdict.get('id') == jogador_atualizado.get_id():
                dados_atualizados.append(jogador_atualizado.to_dict())
                encontrou = True
            else:
                dados_atualizados.append(jdict)
        
        if encontrou:
            self._escrever_arquivo(dados_atualizados)

    def deletar(self, jogador_id):
        """
        Delete do CRUD
        """
        dados = self._ler_arquivo()
        
        dados_filtrados = [j for j in dados if j.get('id') != jogador_id]
        
        if len(dados_filtrados) < len(dados):
            self._escrever_arquivo(dados_filtrados)
            return True
        return False
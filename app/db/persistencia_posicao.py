import json
import os
from app.models.posicao import Posicao

class PersistenciaPosicao:

    FILE_PATH = os.path.join('app', 'db', 'posicoes.json')

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

    def salvar(self, posicao_obj):
        """
        Create do CRUD
        """
        dados = self._ler_arquivo()
        dados.append(posicao_obj.to_dict()) 
        self._escrever_arquivo(dados)
    
    def listar_todos(self):
        """
        Read do CRUD - ler todos
        """
        dados = self._ler_arquivo()
        posicoes = [Posicao.from_dict(p) for p in dados]
        return posicoes

    def buscar_por_id(self, posicao_id):
        """
        Read do CRUD - ler um por um
        """
        dados = self._ler_arquivo()
        for pdict in dados:
            if pdict.get('id') == posicao_id:
                return Posicao.from_dict(pdict)
        return None
    
    def atualizar(self, posicao_id):
        """
        Update do CRUD
        """
        dados = self._ler_arquivo()
        dados_atualizados = []
        encontrou = False
        for pdict in dados:
            if pdict.get('id') == posicao_id.get_id():
                dados_atualizados.append(posicao_id.to_dict())
                encontrou = True
            else:
                dados_atualizados.append(pdict)
        
        if encontrou:
            self._escrever_arquivo(dados_atualizados)

    def deletar(self, posicao_id):
        """
        Delete do CRUD
        """
        dados = self._ler_arquivo()
        
        dados_filtrados = [p for p in dados if p.get('id') != posicao_id]
        
        if len(dados_filtrados) < len(dados):
            self._escrever_arquivo(dados_filtrados)
            return True
        return False
import json
import os
from app.models.time import Time


class PersistenciaTime:

    FILE_PATH = os.path.join('app', 'db', 'times.json')

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

    def salvar(self, time_obj):
        """
        Create do CRUD
        """
        dados = self._ler_arquivo()
        dados.append(time_obj.to_dict()) 
        self._escrever_arquivo(dados)
    
    def listar_todos(self):
        """
        Read do CRUD - ler todos
        """
        dados = self._ler_arquivo()
        times = [Time.from_dict(t) for t in dados]
        return times

    def buscar_por_id(self, time_id):
        """
        Read do CRUD - ler um por um
        """
        dados = self._ler_arquivo()
        for tdict in dados:
            if tdict.get('id') == time_id:
                return Time.from_dict(tdict)
        return None
    
    def atualizar(self, time_atualizado):
        """
        Update do CRUD
        """
        dados = self._ler_arquivo()
        dados_atualizados = []
        for tdict in dados:
            if tdict.get('id') == time_atualizado.get_id():
                dados_atualizados.append(time_atualizado.to_dict())
            else:
                dados_atualizados.append(tdict)
        
        self._escrever_arquivo(dados_atualizados)

    def deletar(self, time_id):
        """
        Delete do CRUD
        """
        dados = self._ler_arquivo()
        dados_filtrados = [t for t in dados if t.get('id') != time_id]
        self._escrever_arquivo(dados_filtrados)
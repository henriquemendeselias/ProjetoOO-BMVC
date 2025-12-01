import json
import os
from app.models.usuario import Usuario

class PersistenciaUsuario:
    
    FILE_PATH = os.path.join('app', 'db', 'usuarios.json')

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
                return json.load(f)
        except:
            return []

    def _escrever_arquivo(self, dados):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4)

    def salvar(self, usuario):
        dados = self._ler_arquivo()
        dados.append(usuario.to_dict())
        self._escrever_arquivo(dados)

    def buscar_por_login(self, nome_login):
        """
        Busca um usuário pelo nome Retorna o objeto Usuario ou None.
        """
        dados = self._ler_arquivo()
        for u_dict in dados:
            if u_dict.get('nome') == nome_login:
                return Usuario.from_dict(u_dict)
        return None
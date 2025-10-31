import uuid

class Posicao:

    def __init__(self, nome, sigla, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.nome = nome
        self.sigla = sigla

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_sigla(self):
        return self.sigla
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "sigla": self.sigla
        }
    
    @staticmethod
    def from_dict(data):
        return Posicao(
            id = data.get("id"),
            nome = data.get("nome"),
            sigla = data.get("sigla")
        ) 

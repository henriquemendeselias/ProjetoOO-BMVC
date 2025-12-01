import uuid

class Usuario:
    def __init__(self, nome, senha, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.nome = nome
        self.senha = senha

    def get_id(self): 
        return self.id
    
    def get_nome(self): 
        return self.nome
    
    def get_senha(self): 
        return self.senha

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "senha": self.senha
        }

    @staticmethod
    def from_dict(data):
        return Usuario(
            id=data.get("id"),
            nome=data.get("nome"),
            senha=data.get("senha")
        )
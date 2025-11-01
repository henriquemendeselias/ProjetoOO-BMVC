import uuid

class Time:
    def __init__(self, nome, tipo, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.nome = nome
        self.tipo = tipo

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_tipo(self):
        return self.tipo
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo
        }
    
    @staticmethod
    def from_dict(data):
        return Time(
            id = data.get("id"),
            nome = data.get("nome"),
            tipo = data.get("tipo")
        ) 
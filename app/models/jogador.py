import uuid

class Jogador:
    
    def __init__(self, nome, posicao_id, numero_camisa, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.nome = nome
        self.posicao_id = posicao_id
        self.numero_camisa = numero_camisa

    def get_id(self):
        return self.id
        
    def get_nome(self):
        return self.nome
        
    def get_posicao_id(self):
        return self.posicao_id
        
    def get_numero_camisa(self):
        return self.numero_camisa

    def set_nome(self, nome):
        self.nome = nome
        
    def set_posicao(self, posicao):
        self.posicao = posicao
        
    def set_numero_camisa(self, numero_camisa):
        self.numero_camisa = numero_camisa

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "posicao_id": self.posicao_id,
            "numero_camisa": self.numero_camisa
        }

    @staticmethod
    def from_dict(data):
        return Jogador(
            id=data.get("id"),
            nome=data.get("nome"),
            posicao_id=data.get("posicao_id"),
            numero_camisa=data.get("numero_camisa")
        )
import uuid
from datetime import datetime

class Jogador:
    
    def __init__(self, nome, posicao_id, numero_camisa, time_id, data_nascimento, nacionalidade, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.nome = nome
        self.posicao_id = posicao_id
        self.time_id = time_id
        self.numero_camisa = numero_camisa
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade

    def get_id(self):
        return self.id
        
    def get_nome(self):
        return self.nome
        
    def get_posicao_id(self):
        return self.posicao_id
        
    def get_numero_camisa(self):
        return self.numero_camisa
    
    def get_time_id(self):
        return self.time_id
    
    def get_data_nascimento(self):
        return self.data_nascimento
    
    def get_nacionalidade(self):
        return self.nacionalidade

    def set_nome(self, nome):
        self.nome = nome
        
    def set_posicao(self, posicao):
        self.posicao = posicao
        
    def set_numero_camisa(self, numero_camisa):
        self.numero_camisa = numero_camisa

    def get_idade(self):
        """
        Calcula a idade do jogador com base na data de nascimento.
        """
        if not self.data_nascimento:
            return "?"
        
        try:
            hoje = datetime.now()
            nasc = datetime.strptime(self.data_nascimento, "%Y-%m-%d")
            idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            return idade
        except ValueError:
            return "?"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "posicao_id": self.posicao_id,
            "time_id": self.time_id,
            "numero_camisa": self.numero_camisa,
            "data_nascimento": self.data_nascimento,
            "nacionalidade": self.nacionalidade
        }

    @staticmethod
    def from_dict(data):
        return Jogador(
            id=data.get("id"),
            nome=data.get("nome"),
            posicao_id=data.get("posicao_id"),
            time_id=data.get("time_id"),
            numero_camisa=data.get("numero_camisa"),
            data_nascimento= data.get("data_nascimento"),
            nacionalidade=data.get("nacionalidade")
        )
from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, cpf, email=0, endereco=0):
        super().__init__(nome, cpf, email, endereco)

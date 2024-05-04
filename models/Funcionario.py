from .Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, email, endereco, clt=0):
        super().__init__(nome, cpf, email, endereco)
        self.clt = clt
        
        
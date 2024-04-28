from .Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, telefone, cpf, email, endereco, clt=0):
        super().__init__(nome, telefone, cpf, email, endereco)
        self.clt = clt
        
        
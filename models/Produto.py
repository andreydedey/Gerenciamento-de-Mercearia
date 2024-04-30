from .Categoria import Categoria

class Produto:
    def __init__(self, nome, preco, categoria: Categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

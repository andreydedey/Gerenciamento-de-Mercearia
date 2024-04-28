from . import Produto
from datetime import datetime

class Vendas:
    def __init__(self, itensVendido: Produto, vendedor, comprador, quantidadeVendida, data = datetime.now()):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data
from datetime import datetime

class Venda:
    def __init__(self, itensVendido, vendedor, comprador, quantidadeVendida, data=datetime.now().strftime('%d/%m/%y')):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data
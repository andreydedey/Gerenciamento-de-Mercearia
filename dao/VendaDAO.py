import os
import csv
from models.Venda import Venda


class VendaDAO:
    ARQUIVO = os.path.join("db", "venda.csv")
    fieldnames = ["item", "vendedor", "comprador", "quantidadeVendida", "data"]


    @classmethod
    def saveSale(cls, venda: Venda):
        with open(cls.ARQUIVO, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            writer.writerow ({
                "item": venda.itensVendido,
                "vendedor": venda.vendedor,
                "comprador": venda.comprador,
                "quantidadeVendida": venda.quantidadeVendida,
                "data": venda.data
            })

    
    @classmethod
    def readSales(cls):
        with open(cls.ARQUIVO, "r") as file:
            reader = csv.DictReader(file, fieldnames=cls.fieldnames)
            # Pular cabeçalho
            next(reader)
            reader = list(reader)

        return reader

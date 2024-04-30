import os
import csv
from models.Produto import Produto

class ProdutoDAO:
    ARQUIVO = os.path.join("db", "produtos.csv")

    
    @classmethod
    def findProduct(cls, product_name) -> int:
        with open(cls.ARQUIVO, "r") as file:
            fieldnames = ["Nome", "Preco", "Categoria"]
            reader = csv.DictReader(file)
            line = 0
            for row in reader:
                line += 1
                if row["Nome"] == product_name:
                    return line

            # Não encontrou o produto
            return -1 


    @classmethod
    def saveProduct(cls, produto: Produto) -> bool:
        with open(cls.ARQUIVO, "a", newline='') as file:
            fieldnames = ["Nome", "Preco", "Categoria"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "Nome": produto.nome,
                "Preco": produto.preco,
                "Categoria": produto.categoria.categoria
            })

        return True


    @classmethod
    def removeProduct(cls, index):
        with open(cls.ARQUIVO, "r") as file:
            reader = csv.reader(file)
            reader = list(reader)

        with open(cls.ARQUIVO, "w", newline='') as file:
            writer = csv.writer(file)
            linha = 0
            for row in reader:
                if linha != index:
                    writer.writerow(row)
                linha += 1
        
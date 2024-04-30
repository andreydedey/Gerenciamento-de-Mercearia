import os
import csv
from models.Fornecedor import Fornecedor


class FornecedorDAO:
    ARQUIVO = os.path.join("db", "fornecedores.csv")

    @classmethod
    def findSupplier(cls, cnpj):
        with open(cls.ARQUIVO, "r") as file:
            reader = csv.reader(file)
            line = 0
            for row in reader:
                if str(cnpj) in row:
                    return line
                line += 1
            
        #Supplier não encontrado
        return -1

    @classmethod
    def saveSupplier(cls, fornecedor: Fornecedor):
        with open(cls.ARQUIVO, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["nome", "cnpj", "telefone", "categoria"])
            writer.writerow({
                "nome": fornecedor.nome,
                "cnpj": fornecedor.cnpj,
                "telefone": fornecedor.telefone,
                "categoria": fornecedor.categoria.categoria
            })

    
    @classmethod
    def removeSupplier(cls, index):
        with open(cls.ARQUIVO, "r") as file:
            reader = csv.reader(file)
            reader = list(reader)


        with open(cls.ARQUIVO, "w", newline='') as file:
            writer = csv.writer(file)
            line = 0
            for row in reader:
                if line != index:
                    writer.writerow(row)
                line += 1


    @classmethod
    def alterSupplier(cls, index, supplier: Fornecedor):
        with open(cls.ARQUIVO, "r") as file:
                reader = csv.reader(file)
                reader = list(reader)

        with open(cls.ARQUIVO, "w", newline="") as file:
            writer = csv.writer(file)
            line = 0
            for row in reader:
                if line == index:
                    writer.writerow([supplier.nome, supplier.cnpj, supplier.telefone, supplier.categoria.categoria])
                else:
                    writer.writerow(row)
                line += 1
    

    @classmethod
    def listSuppliers(cls):
        suppliers = []
        with open(cls.ARQUIVO, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                supplier = f"nome: {row["nome"]} cnpj: {row["cnpj"]} telefone: {row["telefone"]} categoria: {row["categoria"]}"
                suppliers.append(supplier)

        return suppliers
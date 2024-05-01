import os
import csv
from models.Cliente import Cliente

class ClienteDAO:
    ARQUIVO = os.path.join("db", "clientes.csv")

    @classmethod
    def findClient(cls, cpf):
        with open(cls.ARQUIVO, "r") as file:
            line = 0
            reader = csv.reader(file)
            for row in reader:
                if str(cpf) in row:
                    return line
                line += 1
        # Não encontrou cliente
        return -1
    

    @classmethod
    def saveClient(cls, cliente: Cliente):
        with open(cls.ARQUIVO, "a", newline='') as file:
            fieldnames=["nome", "cpf", "email", "endereco"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "nome": cliente.nome,
                "cpf": cliente.cpf,
                "email": cliente.email,
                "endereco": cliente.endereco
            })


    @classmethod
    def removeClient(cls, index):
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

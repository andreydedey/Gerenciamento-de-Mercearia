import os
import csv
from models.Funcionario import Funcionario

class FuncionarioDAO:
    ARQUIVO = os.path.join("db", "funcionarios.csv")

    @classmethod
    def findEmploye(cls, cpf):
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
    def saveEmploye(cls, employe: Funcionario):
        with open(cls.ARQUIVO, "a", newline='') as file:
            fieldnames=["nome", "cpf", "email", "endereco"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                "nome": employe.nome,
                "cpf": employe.cpf,
                "email": employe.email,
                "endereco": employe.endereco
            })


    @classmethod
    def removeEmploye(cls, index):
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
    def alterEmploye(cls, index, employe: Funcionario):
        cls.removeClient(index)
        cls.saveClient(employe)

    
    @classmethod
    def listEmployes(cls):
        employes = []
        with open(cls.ARQUIVO, "r") as file:
            fieldnames = ["nome", "cpf", "email", "endereco"]
            reader = csv.DictReader(file, fieldnames=fieldnames)
            next(reader)
            for row in reader:
                employe = f"Nome: {row["nome"]} CPF: {row["cpf"]} email: {row["email"]} endereço: {row["endereco"]}"
                employes.append(employe)
            
        return employes

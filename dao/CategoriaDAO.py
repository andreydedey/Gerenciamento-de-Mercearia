import os
import csv
from models.Categoria import Categoria

class CategoriaDAO:
    arquivo = os.path.join("db", "categoria.csv")


    @classmethod
    def findCategory(cls, categoria: Categoria) -> int:
        with open(cls.arquivo, "r") as file:
            reader = csv.reader(file, delimiter=',')
            reader = list(reader)
            line = 0
            for row in reader:
                if categoria.categoria == row[0]:
                    return line
                line += 1
            # Não encontrou categoria
            return -1
        
    

    @classmethod
    def saveCategory(cls, categoria):
        with open(cls.arquivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([categoria.categoria])


    @classmethod
    def removeCategory(cls, index):
        with open(cls.arquivo, 'r', newline='') as file:
            reader = csv.reader(file)
            reader = list(reader)
        
        with open(cls.arquivo, 'w', newline='') as file:
            writer = csv.writer(file)
            line = 0
            for row in reader:
                if line != index:
                    writer.writerow(reader[line])
                line += 1

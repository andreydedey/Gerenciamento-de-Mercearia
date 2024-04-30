import os
import csv
from models.Categoria import Categoria

class CategoriaDAO:
    ARQUIVO = os.path.join("db", "categoria.csv")


    @classmethod
    def findCategory(cls, categoria: Categoria) -> int:
        with open(cls.ARQUIVO, "r") as file:
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
    def saveCategory(cls, categoria: Categoria):
        with open(cls.ARQUIVO, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([categoria.categoria])


    @classmethod
    def removeCategory(cls, index: int):
        with open(cls.ARQUIVO, 'r', newline='') as file:
            reader = csv.reader(file)
            reader = list(reader)
        
        with open(cls.ARQUIVO, 'w', newline='') as file:
            writer = csv.writer(file)
            line = 0
            for row in reader:
                if line != index:
                    writer.writerow(reader[line])
                line += 1


    @classmethod
    def alterCategory(cls, categoria: Categoria, index: int):
        cls.removeCategory(index)
        cls.saveCategory(categoria)


    @classmethod
    def listCategorys(cls):
        with open(cls.ARQUIVO, 'r', newline='') as file:
            reader = csv.DictReader(file)
            categorys = []
            for row in reader:
                categorys.append(row["Categoria"])
        
        return categorys
    
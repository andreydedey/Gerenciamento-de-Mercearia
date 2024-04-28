import os
import csv
from models.Categoria import Categoria

class CategoriaDAO:
    arquivo = os.path.join("db", "categoria.csv")


    @classmethod
    def findCategory(cls, categoria: Categoria) -> int:
        with open(cls.arquivo, "r") as file:
            reader = csv.reader(file, delimiter=',')
            line = 0
            for row in reader:
                if categoria.categoria in row:
                    return line
                line += 1
        
        # Não encontrou categoria
        return -1
    

    @classmethod
    def registerCategory(cls, categoria):
        with open(cls.arquivo, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([categoria.categoria])

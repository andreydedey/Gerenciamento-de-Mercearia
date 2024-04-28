import os
import csv
from models.Categoria import Categoria

class CategoriaDAO:
    arquivo = os.path.join("db", "categoria.csv")


    @classmethod
    def isCategoryPresent(cls, categoria: Categoria) -> bool:
        with open(cls.arquivo, "r") as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if categoria.categoria in row:
                    return True
        
        return False
    

    @classmethod
    def registerCategory(cls, categoria):
        with open(cls.arquivo, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([categoria.categoria])

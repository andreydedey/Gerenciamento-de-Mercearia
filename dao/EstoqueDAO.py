import os
import csv

class EstoqueDAO:
    ARQUIVO = os.path.join("db", "estoque.csv")
    fieldnames = ["produto", "quantidade"]


    @classmethod
    def listProducts(cls):
        products = []
        with open(cls.ARQUIVO, "r") as file:
            
            reader = csv.DictReader(file, fieldnames=cls.fieldnames)
            next(reader)
            for row in reader:
                product = {
                    "produto": row["produto"],
                    "quantidade": row["quantidade"]
                }
                products.append(product)
            
        return products
    

    @classmethod
    def buy_Product(cls, product_name, amount: int):
        with open(cls.ARQUIVO, "r+") as file:
            reader = csv.DictReader(file, fieldnames=cls.fieldnames)
            for row in reader:
                if row["produto"] == product_name:
                    quantidade = int(row["quantidade"])
                    if quantidade >= amount:
                        cls.removeProduct(product_name=product_name)
                        cls.saveProduct(product_name=product_name, amount= quantidade - amount)
                        
                        return True
            
        return False
            

    @classmethod
    def saveProduct(cls, product_name, amount:int):
        with open(cls.ARQUIVO, "a") as file:
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            writer.writerow({
                "produto": product_name,
                "quantidade": amount
            })


    @classmethod 
    def removeProduct(cls, product_name):
        with open(cls.ARQUIVO, "r") as file:
            linha = 0
            reader = csv.DictReader(file, fieldnames=cls.fieldnames)
            reader = list(reader)
            for row in reader:
                if row["produto"] == product_name:
                    break
                linha += 1
        
        with open(cls.ARQUIVO, "w", newline='') as file:
            count = 0
            writer = csv.DictWriter(file, fieldnames=cls.fieldnames)
            for row in reader:
                if count != linha:
                    writer.writerow({
                        "produto": row["produto"],
                        "quantidade": row["quantidade"]
                    })
                count += 1

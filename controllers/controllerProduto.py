from models.Produto import Produto
from models.Categoria import Categoria
from dao.ProdutoDAO import ProdutoDAO
from dao.CategoriaDAO import CategoriaDAO

class ControllerProduto:
    def cadastrarProduto(self):
        nome_produto = input("Digite o nome do produto para cadastrar: ")

        while True:
            try:
                preco_produto = float(input("Digite o preço do produto para cadastrar: "))
                break
            except ValueError:
                print("valor do produto deve ser um número")

        while True:
            categoria_produto = Categoria(input("Digite a categoria do produto: "))
            if CategoriaDAO.findCategory(categoria_produto) == -1:
                print("Categoria não cadastrada\n")
            else:
                break
                
        produto = Produto(nome_produto, preco_produto, categoria_produto)              

        if ProdutoDAO.saveProduct(produto):
            return f"Produto cadastrado com sucesso!"
        
        return f"Não foi possível cadastrar o produto"
    

    def removerProduto(self):
        nome_produto = input("Digite o nome do produto que você deseja remover: ")
        index = ProdutoDAO.findProduct(nome_produto)
        if index == -1:
            return f"Produto não cadastrado"
        
        ProdutoDAO.removeProduct(index)
        return f"Produto removido com sucesso"

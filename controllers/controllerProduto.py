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
            return f"Produto {nome_produto} cadastrado com sucesso!"
        
        return f"Não foi possível cadastrar o produto {nome_produto}"
    

    def removerProduto(self):
        nome_produto = input("Digite o nome do produto que você deseja remover: ")
        index = ProdutoDAO.findProduct(nome_produto)
        if index == -1:
            return f"Produto {nome_produto} não cadastrado"
        
        ProdutoDAO.removeProduct(index)
        return f"Produto {nome_produto} removido com sucesso"


    def alterarProduto(self):
        nome_produto = input("Digite o nome do produto que você deseja alterar: ").strip()
        index = ProdutoDAO.findProduct(nome_produto)
        print(index)
        if index == -1:
            return f"\nProduto {nome_produto} não cadastrado"
        novo_produto = input("Digite o novo nome do produto: ")
        novo_preco = float(input("Digite o novo preço do produto: "))

        # Lógica para verificar categoria
        while True:
            nova_categoria = Categoria(input("Digite nova categoria: ").strip())
            if nova_categoria == "":
                break
            if CategoriaDAO.findCategory(nova_categoria) == -1:
                print("\nCategoria não cadastrada")
            else:
                break

        new_product = Produto(nome=novo_produto, preco=novo_preco, categoria=nova_categoria)
        
        ProdutoDAO.alterProduct(index, new_product)
        return f"\nProduto alterado com sucesso!"
    

    def listarProdutos(self):
        produtos = ProdutoDAO.getProducts()
        for produto in produtos:
            print(produto)
            
        return f"Done!"

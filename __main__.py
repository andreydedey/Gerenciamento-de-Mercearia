import os
from controllers.controllerCategoria import ControllerCategoria
from controllers.controllerProduto import ControllerProduto
from models.Categoria import Categoria
from models.Produto import Produto

def criaArquivo(*nome):
    for i in nome:
        if not os.path.exists("db"):
            os.mkdir("db")
        arquivo_path = os.path.join("db", i)
        if not os.path.exists(arquivo_path):
            with open(arquivo_path, "w") as arq:
                arq.write("")


criaArquivo("categoria.csv", "produtos.csv", "clientes.csv", "estoque.csv", "fornecedores.csv", "funcionarios.csv", "venda.csv")



def categoria():
            categoriaController = ControllerCategoria()
            while True:
                option = int(input("""\nDigite 1 para cadastrar uma categoria
Digite 2 para remover uma categoria
Digite 3 para alterar uma categoria
Digite 4 para mostrar as categorias cadastradas
Digite 5 para sair
Digite: """))
                match option:
                    case 1:
                        categoria = Categoria(input("Digite a categoria para cadastrar: ").strip())

                        message = categoriaController.cadastrarCategoria(categoria)
                        print(message + "\n")
                    
                    case 2:
                        categoria = Categoria(input("Digite a categoria para remover: ").strip())

                        message = categoriaController.removerCategoria(categoria)
                        print(message + "\n")
                    
                    case 3:
                        categoria_para_alterar = Categoria(input("Digite a categoria a ser removida: ").strip())
                        categoria_nova = Categoria(input("Digite a categoria a ser adicionada: ").strip())

                        message = categoriaController.alterarCategoria(categoria_nova, categoria_para_alterar)
                        print(message + "\n")
                    
                    case 4:
                        message = categoriaController.listarCategorias()
                        print(message + "\n")

                    case 5:
                          break


def produto():
    while True:
        produtoController = ControllerProduto()
        local = int(input(
            "Digite 1 para cadastrar um produto\n"
            "Digite 2 para remover um produto\n"
            "Digite 3 para alterar um produto\n"
            "Digite 4 para mostrar os produtos cadastrados\n"
            "Digite 5 para sair\n"))   

        match local:
            case 1:
                message = produtoController.cadastrarProduto()
                print(message + "\n")
            
            case 2:
                message = produtoController.removerProduto()
                print(message + "\n")

            case 5:
                break


if __name__ == "__main__":
        while True:
             
            local = int(input("""Digite 1 para acessar ( Categorias )
Digite 2 para acessar ( Estoque )
Digite 3 para acessar ( Fornecedor )
Digite 4 para acessar ( Cliente )
Digite 5 para acessar ( funcionario )
Digite 6 para acessar ( Vendas )
Digite 7 para acessar ( Produtos )
Digite: """))
            
            match local:
                case 1:
                    categoria()

                case 7:
                    produto()
import os
from controllers.controllerCategoria import ControllerCategoria
from models.Categoria import Categoria

def criaArquivo(*nome):
    for i in nome:
        if not os.path.exists("db"):
            os.mkdir("db")
        arquivo_path = os.path.join("db", i)
        if not os.path.exists(arquivo_path):
            with open(arquivo_path, "w") as arq:
                arq.write("")


criaArquivo("categoria.csv", "clientes.csv", "estoque.csv", "fornecedores.csv", "funcionarios.csv", "venda.csv")

if __name__ == "__main__":
    while True:
        local = int(input("""Digite 1 para acessar ( Categorias )
Digite 2 para acessar ( Estoque )
Digite 3 para acessar ( Fornecedor )
Digite 4 para acessar ( Cliente )
Digite 5 para acessar ( funcionario )
Digite 6 para aessar ( Vendas )
Digite: """))
        
        match local:

            case 1:
                categoriaController = ControllerCategoria()
                while True:
                    option = int(input("""\n\nDigite 1 para cadastrar uma categoria
Digite 2 para remover uma categoria
Digite 3 para alterar uma categoria
Digite 4 para mostrar as categorias cadastradas
Digite 5 para sair
Digite: """))
                    match option:
                        case 1:
                            categoria = Categoria(input("Digite a categoria para cadastrar: "))

                            categoriaController.cadastrarCategoria(categoria)

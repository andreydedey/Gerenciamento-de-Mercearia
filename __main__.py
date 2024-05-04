import os
from controllers.controllerCategoria import ControllerCategoria
from controllers.controllerProduto import ControllerProduto
from controllers.controllerFornecedor import ControllerFornecedor
from controllers.controllerCliente import ControllerCliente
from controllers.controllerFuncionario import ControllerFuncionario
from controllers.controllerEstoque import ControllerEstoque
from controllers.controllerVenda import ControllerVenda
from controllers.controllerRelatorio import ControllerRelatorio
from models.Categoria import Categoria


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
            
            case 3:
                message = produtoController.alterarProduto()
                print(message + "\n")

            case 4:
                message = produtoController.listarProdutos()
                print(message +  "\n")

            case 5:
                break


def fornecedor():
     while True:
        fornecedorController = ControllerFornecedor()
        local = int(input("Digite 1 para cadastrar Fornecedor\n"
                    "Digite 2 para remover um Fornecedor\n"
                    "Digite 3 para alterar um Fornecedor\n"
                    "Digite 4 para mostrar os Fornecedores cadastrados\n"
                    "Digite 5 para sair\n"))

        match local:
            case 1:
                message = fornecedorController.cadastrarFornecedor()
                print(message + "\n")

            case 2:
                message = fornecedorController.removerFornecedor()
                print(message + "\n")
            
            case 3:
                message = fornecedorController.alterarFornecedor()
                print(message + "\n")
            
            case 4:
                message = fornecedorController.listar_fornecedores()
                print(message + "\n")

            case 5:
                break


def estoque():
    controllerEstoque = ControllerEstoque()
    while True:
        local = int(input("1 - Ver produtos em estoque:\n"
                          "2 - Sair:\n"))
        
        match local:
            case 1:
                message = controllerEstoque.listarProdutos()
                print(message + "\n")
            
            case 2:
                break


def cliente():
    while True:
        clienteController = ControllerCliente()
        local = int(input("Digite 1 para cadastrar Cliente\n"
                        "Digite 2 para remover Cliente\n"
                        "Digite 3 para alterar Cliente\n"
                        "Digite 4 para listar Clientes\n"
                        "Digite 5 para sair\n"))

        match local:
            case 1:
                message = clienteController.cadastrarCliente()
                print(message + "\n")
            
            case 2:
                message = clienteController.removerCliente()
                print(message + "\n")

            case 3:
                message = clienteController.alterarCliente()
                print(message + "\n")

            case 4:
                message = clienteController.listarClientes()
                print(message + "\n")

            case 5:
                break


def funcionario():
    while True:
        funcionarioController = ControllerFuncionario()
        local = int(input("Digite 1 para cadastrar Funcionario\n"
                        "Digite 2 para remover Funcionario\n"
                        "Digite 3 para alterar Funcionario\n"
                        "Digite 4 para listar Funcionario\n"
                        "Digite 5 para sair\n"))

        match local:
            case 1:
                message = funcionarioController.cadastrarFuncionario()
                print(message + "\n")
            
            case 2:
                message = funcionarioController.removerFuncionario()
                print(message + "\n")

            case 3:
                message = funcionarioController.alterarFuncionario()
                print(message + "\n")

            case 4:
                message = funcionarioController.listarFuncionarios()
                print(message + "\n")

            case 5:
                break


def venda():
    while True:
        vendaController = ControllerVenda()
        local = int(input("1 - realizar venda:\n"
                        "2 - Sair\n"))

        match local:
            case 1:
                vendaController.realizarVenda()

            case 2:
                break


def relatorio():
    while True:
        relatorioController = ControllerRelatorio()
        local = int(input("1 - Relatório Geral de Vendas:\n"
                          "2 - Relatório de Vendas por Datas:\n"
                          "3 - Relatório de Produtos mais Vendidos\n"
                          "4 - Relatório de clientes que mais compraram\n"))
        
        match local:
            case 1:
                relatorioController.relatorioGeral()

            case 2:
                date = input("Enter a date in DD-MM-YYYY format:")
                relatorioController.produtosVendidosPorData(date)

            case 3:
                print("Produtos mais vendidos em ordem\n")
                relatorioController.produtosMaisVendidos()
            
            case 4:
                relatorioController.clientesQueMaisCompraram()
            


if __name__ == "__main__":
        while True:
             
            local = int(input("""Digite 1 para acessar ( Categorias )
Digite 2 para acessar ( Estoque )
Digite 3 para acessar ( Fornecedor )
Digite 4 para acessar ( Cliente )
Digite 5 para acessar ( funcionario )
Digite 6 para acessar ( Vendas )
Digite 7 para acessar ( Produtos )
Digite 8 para acessar ( Relatórios )                              
Digite: """))
            
            match local:
                case 1:
                    categoria()

                case 2:
                    estoque()
                
                case 3:
                    fornecedor()

                case 4:
                    cliente()

                case 5:
                    funcionario()

                case 6:
                    venda()

                case 7:
                    produto()
                
                case 8:
                    relatorio()

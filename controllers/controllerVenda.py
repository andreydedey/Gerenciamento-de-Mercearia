from dao.ClienteDAO import ClienteDAO
from dao.FuncionarioDAO import FuncionarioDAO
from dao.ProdutoDAO import ProdutoDAO
from dao.EstoqueDAO import EstoqueDAO
from dao.VendaDAO import VendaDAO
from models.Venda import Venda

class ControllerVenda:
    def realizarVenda(self):
        while True:
            cpf_funcionario = input("Funcionário (cpf): ")
            index_funcionario = FuncionarioDAO.findEmploye(cpf_funcionario)
            if index_funcionario == -1:
                print("Funcionário não encontrado")
            else:
                break

        while True:
            cpf_cliente = input("Cliente (cpf): ")
            index_cliente = ClienteDAO.findClient(cpf_cliente)
            if index_cliente == -1:
                print("Cliente não encontrado")
            else:
                break

        while True:
            produto = input("Digite o nome do produto a adicionar: ")

            index_produto = ProdutoDAO.findProduct(product_name=produto)
            if index_produto == -1:
                print(f"Produto {produto} não cadastrado")
                continue

            quantidade_produto = int(input("Digite quantos produtos você quer: "))
            have_product = EstoqueDAO.buy_Product(product_name=produto, amount=quantidade_produto)

            if not have_product:
                print(f"Não há {produto} suficiente no estoque :(")
                continue

            break

        venda = Venda(itensVendido=produto, vendedor=cpf_funcionario, comprador=cpf_cliente, quantidadeVendida=quantidade_produto)

        VendaDAO.saveSale(venda=venda)

        print("Venda concluída")

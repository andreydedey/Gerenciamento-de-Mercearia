from models.Cliente import Cliente
from dao.ClienteDAO import ClienteDAO

class ControllerCliente:
    def cadastrarCliente(self):
        nome = input("Digite o nome do cliente: ")
        cpf = int(input("Digite o cpf do cliente: "))
        email = input("Digite o email do cliente: ")
        endereco = input("Digite o endereço do cliente: ")

        cliente = Cliente(nome=nome, cpf=cpf, email=email, endereco=endereco)
        ClienteDAO.saveClient(cliente=cliente)

        return f"Cliente cadastrado com sucesso!"
            
    
    def removerCliente(self):
        cpf = int(input("Digite o cpf do cliente: "))
        index = ClienteDAO.findClient(cpf=cpf)
        if index == -1:
            return f"Cliente com o cpf {cpf} não cadastrado"
        
        ClienteDAO.removeClient(index)
        return f"Cliente com o cpf {cpf} removido com sucesso"
    

    def alterarCliente(self):
        cpf = int(input("Digite o cpf do cliente: "))
        index = ClienteDAO.findClient(cpf=cpf)
        if index == -1:
            f"Cliente com o cpf {cpf} não cadastrado"

        nome = input("Escreva o nome do cliente: ")
        email = input("Escreva o email do cliente: ")
        endereco = input("Escreve o endereço do cliente: ")

        novo_cliente = Cliente(nome, cpf, email, endereco)

        ClienteDAO.alterClient(index, novo_cliente)
        return f"Cliente alterado com sucesso"


    def listarClientes(self):
        clientes = ClienteDAO.listClients()

        for cliente in clientes:
            print(cliente)
        
        return "Fim"

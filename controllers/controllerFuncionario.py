from models.Funcionario import Funcionario
from dao.FuncionarioDAO import FuncionarioDAO

class ControllerFuncionario:
    def cadastrarFuncionario(self):
        nome = input("Digite o nome do funcionario: ")
        cpf = int(input("Digite o cpf do funcionario: "))
        email = input("Digite o email do funcionario: ")
        endereco = input("Digite o endereço do funcionario: ")

        funcionario = Funcionario(nome=nome, cpf=cpf, email=email, endereco=endereco)
        FuncionarioDAO.saveEmploye(employe=funcionario)

        return f"Funcionário cadastrado com sucesso!"
            
    
    def removerFuncionario(self):
        cpf = int(input("Digite o cpf do funcionario: "))
        index = FuncionarioDAO.findEmploye(cpf=cpf)
        if index == -1:
            return f"Funcionário com o cpf {cpf} não cadastrado"
        
        FuncionarioDAO.removeEmploye(index)
        return f"Funcionário com o cpf {cpf} removido com sucesso"
    

    def alterarFuncionario(self):
        cpf = int(input("Digite o cpf do funcionário: "))
        index = FuncionarioDAO.findEmploye(cpf=cpf)
        if index == -1:
            f"Funcionário com o cpf {cpf} não cadastrado"

        nome = input("Escreva o nome do funcionário: ")
        email = input("Escreva o email do funcionário: ")
        endereco = input("Escreve o endereço do funcionário: ")

        novo_funcionario = Funcionario(nome, cpf, email, endereco)

        FuncionarioDAO.alterClient(index, novo_funcionario)
        return f"Funcionario alterado com sucesso"


    def listarFuncionarios(self):
        funcionarios = FuncionarioDAO.listEmployes()

        for funcionario in funcionarios:
            print(funcionario)
        
        return "Fim"

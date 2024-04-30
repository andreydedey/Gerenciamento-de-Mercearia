from models.Fornecedor import Fornecedor
from models.Categoria import Categoria
from dao.FornecedorDAO import FornecedorDAO
from dao.CategoriaDAO import CategoriaDAO

class ControllerFornecedor:
    def cadastrarFornecedor(self):
        nome_fornecedor = input("Digite o nome do fornecedor: ")
        cnpj_fornecedor = int(input("Digite o cnpj do fornecedor: "))
        tel_fornecedor = int(input("Digite o telefone do fornecedor: "))

        while True:
            categoria_fornecedor = (Categoria(input("Digite a categoria do fornecedor: ")))
            index = CategoriaDAO.findCategory(categoria_fornecedor)
            if index < 0:
                print("Categoria não cadastrada")
            else:
                break
        
        fornecedor = Fornecedor(nome=nome_fornecedor, cnpj=cnpj_fornecedor, telefone=tel_fornecedor, categoria=categoria_fornecedor)
        FornecedorDAO.saveSupplier(fornecedor=fornecedor)

        return f"Fornecedor {fornecedor.nome} cadastrado com sucesso!"
    

    def removerFornecedor(self):
        cnpj_fornecedor = int(input("Digite o cnpj do fornecedor: "))
        index = FornecedorDAO.findSupplier(cnpj=cnpj_fornecedor)
        if index == -1:
            return f"Fornecedor com o cnpj {cnpj_fornecedor} não cadastrado!"
        
        FornecedorDAO.removeSupplier(index)
        return f"Fornecedor com o cnpj {cnpj_fornecedor} removido com sucesso!"


    def alterarFornecedor(self):
        cnpj_fornecedor = input("Digite o cnpj do fornecedor que você deseja alterar: ").strip()
        index = FornecedorDAO.findSupplier(cnpj_fornecedor)
        print(index)
        if index == -1:
            return f"\nFornecedor com o cnpj {cnpj_fornecedor} não cadastrado"
        novo_fornecedor = input("Digite o novo nome do fornecedor: ")
        novo_cnpj = int(input("Digite o novo cnpj do produto: "))
        novo_telefone = int(input("Digite o novo telefone: "))

        # Lógica para verificar categoria
        while True:
            nova_categoria = Categoria(input("Digite nova categoria: ").strip())
            if nova_categoria == "":
                break
            if CategoriaDAO.findCategory(nova_categoria) == -1:
                print("\nCategoria não cadastrada")
            else:
                break

        new_supplier = Fornecedor(nome=novo_fornecedor, cnpj=novo_cnpj, telefone=novo_telefone, categoria=nova_categoria)
        
        FornecedorDAO.alterSupplier(index, new_supplier)
        return f"\nFornecedor alterado com sucesso!"

    
    def listar_fornecedores(self):
        fornecedores = FornecedorDAO.listSuppliers()
        for fornecedor in fornecedores:
            print(fornecedor)
        
        return f"\nFim"

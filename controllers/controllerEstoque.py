from models.Estoque import Estoque
from dao.EstoqueDAO import EstoqueDAO


class ControllerEstoque:
    def listarProdutos(self):
        produtos = EstoqueDAO.listProducts()

        print("\n")
        for produto in produtos:
            print(f"Nome: {produto["produto"]} - Quantidade: {produto["quantidade"]}")

        return f"\nFim"

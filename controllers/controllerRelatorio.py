from datetime import datetime
from dao.VendaDAO import VendaDAO


class ControllerRelatorio:
    def relatorioGeral(self):
        vendas = VendaDAO.readSales()
        for venda in vendas:
            print(f"item: {venda['item']} quantidade vendida: {venda['quantidadeVendida']}")
            print("\n")


    def produtosMaisVendidos(self):
        produtos = {}

        vendas = VendaDAO.readSales()
        for venda in vendas:
            if not venda["item"] in produtos:
                produtos[venda["item"]] = 0
            produtos[venda["item"]] += int(venda["quantidadeVendida"])

        produtos_mais_vendidos = []
        for key in produtos.keys():
            produtos_mais_vendidos.append(key)

        produtos_mais_vendidos.sort(key=lambda x: produtos[x])
        print(produtos_mais_vendidos)

    
    def clientesQueMaisCompraram(self):
        clientes = {}

        vendas = VendaDAO.readSales()
        for venda in vendas:
            if not venda["comprador"] in clientes:
                clientes[venda["comprador"]] = 0
            clientes[venda["comprador"]] += int(venda['quantidadeVendida'])

        clientes_que_mais_compraram = []
        for key in clientes.keys():
            clientes_que_mais_compraram.append(key)
        
        clientes_que_mais_compraram.sort(key=lambda x: clientes[x])
        print(clientes_que_mais_compraram)


    def produtosVendidosPorData(self, date_string):
        data = datetime.strptime(date_string, "%d/%m/%y")
        vendas_apos_data = []

        vendas = VendaDAO.readSales()
        for venda in vendas:
            data_venda = datetime.strptime(venda["data"], "%d/%m/%y")
            if data_venda >= data:
                vendas_apos_data.append(venda)
        
        for venda in vendas_apos_data:
            print(venda)

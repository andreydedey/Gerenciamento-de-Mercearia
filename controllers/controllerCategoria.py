from models.Categoria import Categoria
from dao.CategoriaDAO import CategoriaDAO

class ControllerCategoria:
    def cadastrarCategoria(self, categoria: Categoria):
        if CategoriaDAO.findCategory(categoria) >= 0:
            return f"categoria {categoria.categoria} já está cadastrada!"
        
        CategoriaDAO.saveCategory(categoria)
        return f"categoria {categoria.categoria} cadastrada com sucesso!"
        
    
    def removerCategoria(self, categoria: Categoria):
        index = CategoriaDAO.findCategory(categoria)
        if index >= 0:
            CategoriaDAO.removeCategory(index)
            return f"categoria {categoria.categoria} removida!"
        
        return f"categoria {categoria.categoria} não existe!"


    def alterarCategoria(self, categoria_nova: Categoria, categoria_para_alterar):
        index = CategoriaDAO.findCategory(categoria_para_alterar)
        if index >= 0:
            CategoriaDAO.alterCategory(categoria_nova, index)
            return f"categoria {categoria_para_alterar.categoria} substituída por {categoria_nova.categoria} com sucesso!"

        return f"categoria {categoria_para_alterar.categoria} não existe!"


    def listarCategorias(self):
        categorias = CategoriaDAO.listCategorys()
        print("Categorias cadastradas:\n")
        for categoria in categorias:
            print(categoria)
        
        return f"\nDone!"

from models.Categoria import Categoria
from dao.CategoriaDAO import CategoriaDAO

class ControllerCategoria:
    def cadastrarCategoria(self, categoria: Categoria):
        if CategoriaDAO.isCategoryPresent(categoria):
            return f"categoria {categoria} já está cadastrada!"
        
        CategoriaDAO.registerCategory(categoria)
        return f"categoria {categoria} cadastrada com sucesso!"
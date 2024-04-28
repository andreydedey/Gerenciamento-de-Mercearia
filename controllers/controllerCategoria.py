from models.Categoria import Categoria
from dao.CategoriaDAO import CategoriaDAO

class ControllerCategoria:
    def cadastrarCategoria(self, categoria: Categoria):
        if CategoriaDAO.findCategory(categoria):
            CategoriaDAO.registerCategory(categoria)
            return f"categoria {categoria.categoria} cadastrada com sucesso!"
        
        return f"categoria {categoria.categoria} já está cadastrada!"
        
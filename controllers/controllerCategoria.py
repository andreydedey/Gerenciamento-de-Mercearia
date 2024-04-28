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
                    
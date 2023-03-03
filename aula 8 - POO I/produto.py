"""
Classroom activitie
"""

class Produto:
    """
    This class is responsible for the registration of products
    """
    
    def __init__(self,name: str,valor: float,categ: str,description: str) -> None:
        """
        The __init__ function is the constructor for a class. It is called whenever an object of that class is created.
        The __init__ function can take arguments, but self must be first. The __init__ function cannot return values.
        
        :param self: Reference the object itself
        :param name: str: Set the name of the product
        :param valor: float: Set the value of the product
        :param categ: str: Define the category of the product
        :param description: str: Store the description of the product
        :return: None
        :doc-author: Trelent
        """
        
        self.nome = name
        self.__preco = valor
        self.__categoria = categ
        self.descricao = description
    
    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, new_preco: float) -> None:
        self.__preco = new_preco
    
    @property
    def categoria(self) -> str:
        return self.__categoria
    
    @categoria.setter
    def categoria(self, new_categoria: str) -> None:
        self.__categoria = new_categoria

    def reajustar_preco(self,reajuste: float) -> float:
        """
        The reajustar_preco function takes a float representing the percentage increase in price, and returns the new price.
        
        
        :param self: Access attributes and methods of the class in python
        :param reajuste: float: Indicate the percentage of price increase
        :return: The updated price
        :doc-author: Trelent
        """
        
        self.preco += (self.preco * reajuste/100)
        return(f'Preço atualizado: R${self.preco}')
    
    def __repr__(self):
        #[self.nome,self.__preco,self.__categoria,self.descricao for _ in self.__dict__values]
        return self.nome


        
    
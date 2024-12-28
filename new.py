class Ecommerce:

    """
    Initiliaze a class taking the products in an e-commerce system.
    Then we can define a function taking a the products,
    Parsing them into the class.
    """

    def __init__(self, id:str, price:str, name:str, stock: int=0):
        self.id=id
        self.name= name
        self._price= price
        self._stock= stock
        self._discount= 0
        self._low_stock_threshold=5
        self._stock_history = []
    



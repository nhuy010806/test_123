
class Product:
    def __init__(self, prodId, prodName, prodQty, prodPrice):
        self.prodId = prodId
        self.prodName = prodName
        self.prodQty = prodQty
        self.prodPrice = prodPrice


    def __str__(self):
        return f"{self.prodId}\t{self.prodName}\t{self.prodPrice}\t{self.prodQty}"

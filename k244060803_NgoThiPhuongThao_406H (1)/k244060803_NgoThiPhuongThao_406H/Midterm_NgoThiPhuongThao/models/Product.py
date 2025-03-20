
class Product:
    def __init__(self, prodId, prodName, quantity, prodEntryPrice, proMaketPrice, cateId):
        self.prodId = prodId
        self.prodName = prodName
        self.quantity = quantity

        self.cateId = cateId
        self.proMaketPrice = proMaketPrice
        self.prodEntryPrice = prodEntryPrice


    def __str__(self):
        return f"{self.prodId}\t{self.prodName}\t{self.prodEntryPrice}\t{self.proMaketPrice}\t{self.quantity}\t{self.cateId}"
class Product:
    def __init__(self, proid,proname,price,quantity,cateid,date):
        self.proid = proid
        self.proname = proname
        self.price = price
        self.quantity = quantity
        self.cateid = cateid
        self.date = date
    def __str__(self):
        return (f"{self.proid}\t{self.proname}\t{self.price}\t"
                f"{self.quantity}\t{self.cateid}\t{self.date}")

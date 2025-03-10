class Category(object):
    def __init__(self,cate_id=None, cate_name=None, products=None):
        self.cate_id=cate_id
        self.cate_name=cate_name
        if products==None:
            self.products=[]
        else:
            self.products=products
    def __str__(self):
        return f"{self.cate_id}\t{self.cate_name}"
    def add_product(self,p):
        self.products.append(p)
    def add_products(self,products):
        self.products.extend(products)
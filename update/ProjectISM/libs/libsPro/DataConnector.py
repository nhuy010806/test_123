from libs.JsonFileFactory import JsonFileFactory
from models.Category import Category
from models.Product import Product


class DataConnector:
    def get_all_categories(self):
        categories = []
        jff = JsonFileFactory()
        filename = "../dataset/categories.json"
        categories = jff.read_data(filename, Category)
        return categories
    def get_all_cateids(self):
        cateids = []
        jff = JsonFileFactory()
        filename = "../dataset/categories.json"
        categories = jff.read_data(filename, Category)
        for category in categories:
            cateids.append(category.cateid)
        return cateids
    def get_all_products(self):
        products = []
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        products = jff.read_data(filename, Product)
        return products
    def get_products_by_categories(self,cateid):
        products = self.get_all_products()
        result=[]
        for product in products:
            if product.cateid==cateid:
                result.append(product)
        return result

    def find_index_product(self,proid):
        self.products = self.get_all_products()
        for i, product in enumerate(self.products):
            if product.proid == proid:
                return i
        return -1

    # def delete_product(self,proid):
    #     index=self.find_index_product(proid)
    #     if index!=-1:
    #         self.products.pop(index)
    #         jff = JsonFileFactory()
    #         filename = "../dataset/products.json"
    #         jff.write_data(self.products, filename)
    def delete_products(self, proid_list):

        self.products = self.get_all_products()  
        original_count = len(self.products)


        self.products = [p for p in self.products if p.proid not in proid_list]


        if len(self.products) == original_count:
            return False

        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        jff.write_data(self.products, filename)

        return True

    def get_products_by_date(self, selected_date):
        pass


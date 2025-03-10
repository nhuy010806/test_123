from libs.JsonFactoryFile import JsonFileFactory
from models.Admin import Admin
from models.Product import Product
from models.Staff import Staff

from models.Supplier import Supplier


class DataConnector:
    def get_all_admins(self):
        jff=JsonFileFactory()
        filename="../dataset/admins.json"
        admins =jff.read_data(filename,Admin)
        return admins
    def get_all_suppliers(self):
        jff=JsonFileFactory()
        filename="../dataset/suppliers.json"
        suppliers=jff.read_data(filename,Supplier)
        return suppliers
    def get_all_staffs(self):
        jff=JsonFileFactory()
        filename="../dataset/staffs.json"
        staffs=jff.read_data(filename,Staff)
        return staffs

    def get_all_products(self):
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        products = jff.read_data(filename, Product)
        return products


    def login(self,id,password):
        employees=self.get_all_admins()
        for e in employees:
            if e.adminUsername==id and e.adminPass==password:
                return e
        return None
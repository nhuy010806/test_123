from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Product import Product
from Midterm_NgoThiPhuongThao.models.Employee import Employee


class DataConnector:
    def get_all_products(self):
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        products = jff.read_data(filename,Product)
        return products
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.json"
        employees = jff.read_data(filename,Employee)
        return employees

    def login(self, Username, Password):
        employees=self.get_all_employees()
        for e in employees:
            if e.username==Username and str(e.password)==str(Password):
                return e
        return None
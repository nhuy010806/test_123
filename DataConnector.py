from models.JsonFileFactory import JsonFileFactory
from models.User import Employee


class DataConnector:
    # def get_products_by_categories(self,cateid):
    #     products =self.get_all_products()
    #     result=[]
    #     for product in products:
    #         if product.cateid==cateid:
    #             result.append(product)
    #     return result
    def get_all_employees(self):
        employees = []
        jff = JsonFileFactory()
        filename = "../dataset/employee.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def save_new_employee(self,employee):
        employees=self.get_all_employees()
        employees.append(employee)
        jff = JsonFileFactory()
        filename = "../dataset/employee.json"
        jff.write_data(employees, filename)

    def find_index_employee(self,EmployeeId):
        self.employees=self.get_all_employees()
        for i in range (len(self.employees)):
            employee=self.employees[i]
            if employee.EmployeeId==EmployeeId:
                return i
        return -1
    def save_update_employee(self,curent_employee):
        index=self.find_index_employee(curent_employee.EmployeeId)
        if index!=-1:
            self.employees[index]=curent_employee
            jff = JsonFileFactory()
            filename = "../dataset/employee.json"
            jff.write_data(self.employees, filename)

    def delete_employee(self, EmployeeId):
        index = self.find_index_employee(EmployeeId)
        if index != -1:
            self.employees.pop(index)
            jff = JsonFileFactory()
            filename = "../dataset/employee.json"
            jff.write_data(self.employees, filename)

    def get_employees_by_categories(self,EmployeeId):
        products =self.get_all_employees()
        result=[]
        for product in products:
            if product.EmployeeId==EmployeeId:
                result.append(product)
        return result

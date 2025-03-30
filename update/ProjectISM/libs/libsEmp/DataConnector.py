from libs.JsonFileFactory import JsonFileFactory
from models.Admin import Admin
from models.Employee import Employee


class DataConnector:
    def get_all_admins(self):
        jff = JsonFileFactory()
        filename = "../dataset/admins.json"
        admins = jff.read_data(filename, Admin)
        return admins
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../dataset/employee.json"
        employees = jff.read_data(filename,Employee)
        return employees

    def login1(self, Username, Password):
        employees=self.get_all_employees()
        for e in employees:
            if e.UserName==Username and str(e.Password)==str(Password):
                return e
        return None
    def login2(self, Username, Password):
        admins=self.get_all_admins()
        for e in admins:
            if e.adminUsername==Username and str(e.adminPass)==str(Password):
                return e
        return None
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

    def get_employees_by_categories(self, EmployeeId):
        for employee in self.get_all_employees():
            if employee.EmployeeId == EmployeeId:
                return employee
        return None


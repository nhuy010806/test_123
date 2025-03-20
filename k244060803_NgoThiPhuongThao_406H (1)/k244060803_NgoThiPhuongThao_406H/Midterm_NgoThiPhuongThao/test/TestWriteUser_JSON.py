from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Employee import Employee


Employees=[]
Employees.append(Employee("U1","Coca","Coca1","10"))
Employees.append(Employee("U2","teo","teo2","15"))


print("ds user:")
for a in Employees:
    print(a)
jff=JsonFileFactory()
filename="../dataset/employees.json"
jff.write_data(Employees,filename)
from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Employee import Employee

jff=JsonFileFactory()
filename="../dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("san pham sau khi doc tu file:")
for e in employees:
    print(e)
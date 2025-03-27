from libs.JsonFileFactory import JsonFileFactory
from models.Employee import Employee

jff=JsonFileFactory()
filename="../dataset/employee.json"
users=jff.read_data(filename,Employee)
print("nguoi dung sau khi doc tu file:")
for a in users:
    print(a)
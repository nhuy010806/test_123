from libs.JsonFileFactory import JsonFileFactory
from models.Supplier import Supplier

jff=JsonFileFactory()
filename= "../../dataset/suppliers.json"
users=jff.read_data(filename,Supplier)
print("nguoi dung sau khi doc tu file:")
for a in users:
    print(a)
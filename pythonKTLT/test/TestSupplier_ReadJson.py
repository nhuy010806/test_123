from libs.JsonFactoryFile import JsonFileFactory
from models.Supplier import Supplier


jff=JsonFileFactory()
filename="../dataset/suppliers.json"
suppliers=jff.read_data(filename,Supplier)
print("Danh sach Admin sau khi doc File la: ")
for e in suppliers:
    print(e)
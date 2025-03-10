from libs.JsonFactoryFile import JsonFileFactory
from models.Product import Product

jff=JsonFileFactory()
filename="../dataset/products.json"
products=jff.read_data(filename,Product)
print("Danh sach kho hang sau khi doc File la: ")
for e in products:
    print(e)
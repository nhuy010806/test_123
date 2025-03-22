from libs.JsonFileFactory import JsonFileFactory
from models.Product import Product

products=[]
jff=JsonFileFactory()
filename="../dataset/products.json"
products=jff.read_data(filename,Product)
print("List of Products after loading Json: ")
for product in products:
    print(product)

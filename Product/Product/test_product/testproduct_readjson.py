from PRODUCT.libs.JsonFileFactory import JsonFileFactory
from PRODUCT.models.Product import Product

products=[]
jff=JsonFileFactory()
filename= "../dataset_product/products.json"
products=jff.read_data(filename,Product)
print("List of Products after loading Json: ")
for product in products:
    print(product)

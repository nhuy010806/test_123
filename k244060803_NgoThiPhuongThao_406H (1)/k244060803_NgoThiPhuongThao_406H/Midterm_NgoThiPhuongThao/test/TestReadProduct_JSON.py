from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Product import Product

jff=JsonFileFactory()
filename="../dataset/products.json"
products=jff.read_data(filename,Product)
print("san pham sau khi doc tu file:")
for p in products:
    print(p)
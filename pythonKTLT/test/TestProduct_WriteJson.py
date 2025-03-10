from libs.JsonFactoryFile import JsonFileFactory
from models.Product import Product

products = []
products.append(Product(1, "Laptop", 10, 1500.0))
products.append(Product(2, "Mouse", 50, 20.0))
products.append(Product(3, "Keyboard", 30, 50.0))
products.append(Product(4, "Monitor", 15, 300.0))
products.append(Product(5, "Headphones", 25, 100.0))
products.append(Product(6, "Smartphone", 20, 800.0))
products.append(Product(7, "Tablet", 12, 600.0))
products.append(Product(8, "Smartwatch", 18, 250.0))
products.append(Product(9, "Camera", 8, 1200.0))
products.append(Product(10, "Printer", 5, 500.0))

print("Danh sách sản phẩm: ")
for p in products:
    print(p)

jff = JsonFileFactory()
filename = "../dataset/products.json"
jff.write_data(products, filename)

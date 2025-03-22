from libsPro.DataConnector import DataConnector

dc=DataConnector()
products=dc.get_all_products()
print("List of Products in database:")
for product in products:
    print(product)
C10="C10"
products_C10=dc.get_products_by_categories(C10)
print("*"*20)
print("List of Products by Category = C10:")
for product in products:
    print(product)
print("=>",len(products_C10))
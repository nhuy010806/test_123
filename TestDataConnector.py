from models.DataConnector import DataConnector

dc=DataConnector()
employees=dc.get_all_employees()
print("list of employees in database: ")
for emp in employees:
    print(emp)

# c10="c10"
# products_c10=dc.get_products_by_categories(c10)
# print("*"*20)
# print("list of product by category = c10: ")
# for product in products_c10:
#     print(product)
# print("=>",len(products_c10))
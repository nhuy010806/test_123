from PRODUCT.libs.DataConnector import DataConnector

dc=DataConnector()
# categories=dc.get_all_categories()
# print("List of Categories in database:")
# for cate in categories:
#     print(cate)
# categories=dc.get_all_cateids()
# print("List of Categories in database:")
# for cate in categories:
#     print(cate)
products=dc.get_all_products()
print("List of Products in database:")
for product in products:
    print(product)
C10="C10"
products_C10=dc.get_product_ids_by_category(C10)
print("*"*20)
print("List of Products by Category = C10:")
for product in products:
    print(product)
print("=>",len(products_C10))
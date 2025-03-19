from DOAN.libs.DataConnector import DataConnector

dc=DataConnector()
categories=dc.get_all_categories()
print("List of categories in database:")
for cate in categories:
    print(cate)

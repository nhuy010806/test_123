from DoAn.libs.DataConnector import DataConnector
dc=DataConnector()
suppliers=dc.get_all_suppliers()
print("list of suppliers in database: ")
for sup in suppliers:
    print(sup)

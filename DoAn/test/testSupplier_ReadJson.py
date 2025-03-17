from DoAn.libs.JsonFileFactory import JsonFileFactory
from DoAn.models.Supplier import Supplier

suppliers=[]
jff=JsonFileFactory()
filename="../dataset/suppliers.json"
categories=jff.read_data(filename,Supplier)
print("Danh sách các nhà cung cấp sau khi đọc File là:")
for sup in suppliers:
    print(sup)
from libs.JsonFileFactory import JsonFileFactory
from models.Admin import Admin

jff=JsonFileFactory()
filename="../../dataset/admins.json"
admins=jff.read_data(filename,Admin)
print("Danh sach Admin sau khi doc File la: ")
for e in admins:
    print(e)

from libs.JsonFactoryFile import JsonFileFactory
from models.Staff import Staff

jff=JsonFileFactory()
filename="../dataset/staffs.json"
staffs=jff.read_data(filename,Staff)
print("Danh sach Admin sau khi doc File la: ")
for e in staffs:
    print(e)
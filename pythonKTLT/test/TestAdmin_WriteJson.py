from libs.JsonFactoryFile import JsonFileFactory
from models.Admin import Admin

admins = []
admins.append(Admin("ADMIN1", "Nguyễn Văn A", "admin.nguyen", "admin123"))
admins.append(Admin("ADMIN2", "Trần Thị B", "admin.tran", "admin234"))
admins.append(Admin("ADMIN3", "Lê Hoàng C", "admin.le", "admin345"))
admins.append(Admin("ADMIN4", "Phạm Thị D", "admin.pham", "admin456"))
admins.append(Admin("ADMIN5", "Đỗ Văn E", "admin.do", "admin567"))

print("Danh sách quản trị viên:")
for a in admins:
    print(a)

jff = JsonFileFactory()
filename = "../dataset/admins.json"
jff.write_data(admins, filename)
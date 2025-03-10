from libs.DataConnector import DataConnector

dc=DataConnector()
admins=dc.get_all_admins()
print("Danh sach admin la: ")
for i in admins:
    print(i)

suppliers=dc.get_all_suppliers()
print("Danh sach nha cung cap la: ")
for a in suppliers:
    print(a)
staffs=dc.get_all_staffs()
print("Danh sach quan li tai san la:")
for staff in staffs:
    print(staff)
uid="AD7"
pwd="129"
emp=dc.login(uid,pwd)
if emp==None:
    print("Đăng nhập thất bại")
else:
    print("Đăng nhập thành công")
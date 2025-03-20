from Midterm_NgoThiPhuongThao.libs.DataConnector import DataConnector

dc=DataConnector()
#lay toan bo nv
employees=dc.get_all_employees()
print("ds users: ")
for e in employees:
    print(e)
#lay toan bo sach
products=dc.get_all_products()
print("ds sản phẩm: ")
for p in products:
    print(p)
# #lay toan bo ds phan cong quan li tai san
# aes=dc.get_all_employee_assets()
# print("ds phan cong quan li: ")
# for ae in aes:
#     print(ae)

#test chuc nang dang nhap he thong
uid="teo2"
pwd="15"
emp=dc.login(uid,int(pwd))
if emp:
    print("\nĐăng nhập thành công!")
else:
    print("\nĐăng nhập thất bại! Vui lòng kiểm tra lại tên đăng nhập hoặc mật khẩu.")
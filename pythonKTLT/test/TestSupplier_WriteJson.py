from libs.JsonFactoryFile import JsonFileFactory
from models.Supplier import Supplier

suppliers = []
suppliers.append(Supplier("SUP1", "Công ty TNHH ABC", "pass123", "Nguyễn Văn An", "contact@abc.com", "0123456789", "Số 123, Đường Hoàng Hoa Thám, Ba Đình, Hà Nội"))
suppliers.append(Supplier("SUP2", "Công ty CP XYZ", "xyzpass", "Trần Thị Bích", "contact@xyz.com", "0987654321", "Số 456, Đường Nguyễn Trãi, Quận 5, TP. Hồ Chí Minh"))
suppliers.append(Supplier("SUP3", "Công ty TNHH MNO", "mno789", "Lê Văn Cường", "contact@mno.com", "0345678912", "Số 789, Đường Lê Lợi, Hải Châu, Đà Nẵng"))
suppliers.append(Supplier("SUP4", "Công ty CP PQR", "pqrsecure", "Phạm Thị Dung", "contact@pqr.com", "0567891234", "Số 321, Đường Ngô Quyền, Ninh Kiều, Cần Thơ"))
suppliers.append(Supplier("SUP5", "Công ty TNHH STU", "stu456", "Hoàng Văn Long", "contact@stu.com", "0678912345", "Số 654, Đường Trần Hưng Đạo, TP. Huế"))
suppliers.append(Supplier("SUP6", "Công ty CP VWX", "vwxpass", "Bùi Thị Lan", "contact@vwx.com", "0789123456", "Số 987, Đường Lê Thánh Tông, Quận Ngô Quyền, Hải Phòng"))
suppliers.append(Supplier("SUP7", "Công ty TNHH YZA", "yzapass", "Đặng Văn Minh", "contact@yza.com", "0891234567", "Số 741, Đường Bình Dương, Thủ Dầu Một, Bình Dương"))
suppliers.append(Supplier("SUP8", "Công ty CP BCD", "bcdpass", "Phạm Văn Hải", "contact@bcd.com", "0901234567", "Số 852, Đường Cao Thắng, Hạ Long, Quảng Ninh"))
suppliers.append(Supplier("SUP9", "Công ty TNHH EFG", "efg789", "Nguyễn Thị Hoa", "contact@efg.com", "0912345678", "Số 963, Đường Hoàng Văn Thụ, TP. Bắc Giang"))
suppliers.append(Supplier("SUP10", "Công ty CP HIJ", "hijpass", "Lê Văn Thành", "contact@hij.com", "0923456789", "Số 147, Đường Nguyễn Chí Thanh, TP. Thanh Hóa"))
suppliers.append(Supplier("SUP11", "Công ty TNHH KLM", "klm321", "Trương Thị Cẩm", "contact@klm.com", "0934567891", "Số 258, Đường Lê Duẩn, TP. Vinh, Nghệ An"))
suppliers.append(Supplier("SUP12", "Công ty CP NOP", "nop654", "Đỗ Văn Hưng", "contact@nop.com", "0945678912", "Số 369, Đường Phan Đình Phùng, TP. Hà Tĩnh"))
suppliers.append(Supplier("SUP13", "Công ty TNHH QRS", "qrs963", "Ngô Thị Mai", "contact@qrs.com", "0956789123", "Số 753, Đường Hùng Vương, TP. Đông Hà, Quảng Trị"))
suppliers.append(Supplier("SUP14", "Công ty CP TUV", "tuvpass", "Võ Văn Bình", "contact@tuv.com", "0967891234", "Số 852, Đường Đồng Khởi, TP. Biên Hòa, Đồng Nai"))
suppliers.append(Supplier("SUP15", "Công ty TNHH WXY", "wxypass", "Tô Thị Oanh", "contact@wxy.com", "0978912345", "Số 951, Đường Trần Phú, TP. Phan Thiết, Bình Thuận"))

print("Danh sách nhà cung cấp:")
for s in suppliers:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/suppliers.json"
jff.write_data(suppliers, filename)

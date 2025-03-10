from libs.JsonFactoryFile import JsonFileFactory
from models.Staff import Staff

staffs = []
staffs.append(Staff("STAFF1", "Nguyễn Văn An", "Số 123, Đường Lê Lợi, Phường 1, Quận 1, TP. Hồ Chí Minh", "an.nguyen", "password123"))
staffs.append(Staff("STAFF2", "Trần Thị Bích", "Số 456, Đường Nguyễn Trãi, Phường 5, Quận 5, TP. Hồ Chí Minh", "bich.tran", "password234"))
staffs.append(Staff("STAFF3", "Lê Hoàng Cường", "Số 789, Đường Hoàng Hoa Thám, Phường 7, Quận Bình Thạnh, TP. Hồ Chí Minh", "cuong.le", "password345"))
staffs.append(Staff("STAFF4", "Phạm Thị Dung", "Số 321, Đường Phan Chu Trinh, Phường 2, TP. Đà Nẵng", "dung.pham", "password456"))
staffs.append(Staff("STAFF5", "Đỗ Văn Hiếu", "Số 654, Đường Trần Hưng Đạo, Phường 3, TP. Hải Phòng", "hieu.do", "password567"))
staffs.append(Staff("STAFF6", "Bùi Thị Lan", "Số 987, Đường Lê Thánh Tông, Phường 6, TP. Hà Nội", "lan.bui", "password678"))
staffs.append(Staff("STAFF7", "Võ Hoàng Minh", "Số 741, Đường Nguyễn Huệ, Phường 4, TP. Nha Trang", "minh.vo", "password789"))
staffs.append(Staff("STAFF8", "Ngô Thị Ngọc", "Số 852, Đường Bạch Đằng, Phường 8, TP. Huế", "ngoc.ngo", "password890"))
staffs.append(Staff("STAFF9", "Trương Văn Phát", "Số 963, Đường Hai Bà Trưng, Phường 9, TP. Cần Thơ", "phat.truong", "password901"))
staffs.append(Staff("STAFF10", "Đặng Thị Quỳnh", "Số 147, Đường Phạm Ngũ Lão, Phường 10, TP. Biên Hòa", "quynh.dang", "password012"))

print("Danh sách nhân viên: ")
for s in staffs:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/staffs.json"
jff.write_data(staffs, filename)
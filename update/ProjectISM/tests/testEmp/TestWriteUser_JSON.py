from libs.JsonFileFactory import JsonFileFactory
from models.Employee import Employee

Users=[]
Users.append(Employee("U1", "Nguyễn Văn An", "staff", "123", "staff", "an@company.com", "Graduated", "Shift 1", "0987600001", "Hà Nội"))
Users.append(Employee("U2", "Trần Thị Bình", "Binh234", "Pass2@123", "staff", "binh@company.com", "Undergraduated", "Shift 2", "0987600002", "Hải Phòng"))
Users.append(Employee("U3", "Lê Văn Châu", "Chau345", "Pass3@123", "staff", "chau@company.com", "Graduated", "Shift 3", "0987600003", "Đà Nẵng"))
Users.append(Employee("U4", "Phạm Thị Duy", "Duy456", "Pass4@123", "admin", "duy@company.com", "Graduated", "Shift 1", "0987600004", "Hồ Chí Minh"))
Users.append(Employee("U5", "Hoàng Văn Em", "Em567", "Pass5@123", "staff", "em@company.com", "Undergraduated", "Shift 2", "0987600005", "Cần Thơ"))
Users.append(Employee("U6", "Ngô Thị Phong", "Phong678", "Pass6@123", "staff", "phong@company.com", "Graduated", "Shift 3", "0987600006", "Bắc Ninh"))
Users.append(Employee("U7", "Đinh Văn Gia", "Gia789", "Pass7@123", "admin", "gia@company.com", "Graduated", "Shift 1", "0987600007", "Quảng Ninh"))
Users.append(Employee("U8", "Bùi Thị Hiếu", "Hieu890", "Pass8@123", "admin", "hieu@company.com", "Undergraduated", "Shift 2", "0987600008", "Thanh Hóa"))
Users.append(Employee("U9", "Vũ Văn Khanh", "Khanh901", "Pass9@123", "staff", "khanh@company.com", "Graduated", "Shift 3", "0987600009", "Nam Định"))
Users.append(Employee("U10", "Phan Thị Linh", "Linh012", "Pass10@123", "staff", "linh@company.com", "Undergraduated", "Shift 1", "0987600010", "Nghệ An"))
for i in range(11, 51):
    Users.append(Employee(
        f"U{i}", f"Nhân Viên {i}", f"User{i}", f"Pass{i}@123",
        "staff" if i % 2 == 0 else "admin", f"user{i}@company.com",
        "Graduated" if i % 2 == 0 else "Undergraduated",
        f"Shift {1 if i % 2 == 0 else 2}", f"09876000{i:02}", f"Thành phố {i}"
    ))

print("ds employee:")
for a in Users:
    print(a)
jff=JsonFileFactory()
filename="../../dataset/employee.json"
jff.write_data(Users,filename)



print("ds employee:")
for a in Users:
    print(a)
jff=JsonFileFactory()
filename="../../dataset/employee.json"
jff.write_data(Users,filename)
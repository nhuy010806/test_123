from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.SinhVien import SinhVien

jff=JsonFileFactory()
filename="../dataset/sinhvien.json"
SinhViens=jff.read_data(filename,SinhVien)
print("sv sau khi doc tu file:")
for a in SinhViens:
    print(a)
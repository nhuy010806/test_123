from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.SinhVien import SinhVien

SinhViens=[]
SinhViens.append(SinhVien("U1","Coca","Coca1",10,11,1))


print("ds sinhvien:")
for a in SinhViens:
    print(a)
jff=JsonFileFactory()
filename="../dataset/sinhvien.json"
jff.write_data(SinhViens,filename)
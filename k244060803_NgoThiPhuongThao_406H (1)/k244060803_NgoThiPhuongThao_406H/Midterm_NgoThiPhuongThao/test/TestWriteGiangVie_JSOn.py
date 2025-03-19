from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.GiangVien import GiangVien

GiangViens=[]
GiangViens.append(GiangVien("U2","teo","teo2",15,"kte"))
GiangViens.append(GiangVien("U3","ty","ty3",20,"luat"))

print("ds gv:")
for a in GiangViens:
    print(a)
jff=JsonFileFactory()
filename="../dataset/giangvien.json"
jff.write_data(GiangViens,filename)
from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.GiangVien import GiangVien

giangvien=[]
giangvien.append(GiangVien("GV01","A","thao","123","KHOAA"))
giangvien.append(GiangVien("GV02","B","ti","456","KHOAB"))
giangvien.append(GiangVien("GV03","C","teo","789","KHOAC"))
jff=JsonFileFactory()
filename="../dataset/giangvien.json"
jff.write_data(giangvien,filename)
for gv in giangvien:
    print(gv)


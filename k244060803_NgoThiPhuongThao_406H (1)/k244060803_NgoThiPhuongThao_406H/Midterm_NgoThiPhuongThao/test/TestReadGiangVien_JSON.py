from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.GiangVien import GiangVien

jff=JsonFileFactory()
filename="../dataset/giangvien.json"
books=jff.read_data(filename,GiangVien)
print("gv sau khi doc tu file:")
for a in books:
    print(a)
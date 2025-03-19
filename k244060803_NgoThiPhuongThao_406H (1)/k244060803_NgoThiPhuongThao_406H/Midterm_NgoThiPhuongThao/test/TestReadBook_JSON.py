from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Book import Book

jff=JsonFileFactory()
filename="../dataset/books.json"
books=jff.read_data(filename,Book)
print("sach sau khi doc tu file:")
for a in books:
    print(a)
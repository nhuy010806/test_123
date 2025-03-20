from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Book import Book

Books=[]
Books.append(Book("B1","Tinh Ta Pho Kiem","Thanh",2001,10))
Books.append(Book("B2","Cuu Am Chan Kinh","Tran",2011,11))
Books.append(Book("B3","That Tich","Duy",2101,12))
Books.append(Book("B4","Bich Huyet Kiem","Nguyen",2003,13))
Books.append(Book("B5","Nhat Duong Chi","Thao",2501,14))

print("ds book:")
for a in Books:
    print(a)
jff=JsonFileFactory()
filename="../dataset/books.json"
jff.write_data(Books,filename)
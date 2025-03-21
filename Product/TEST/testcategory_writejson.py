from libs.JsonFileFactory import JsonFileFactory
from models.Category import Category

categories=[]
categories.append(Category("Trái cây"))
categories.append(Category("Rau củ"))
categories.append(Category("Thực phẩm hữu cơ"))
categories.append(Category("Nông sản địa phương"))
categories.append(Category("Thảo mộc & Gia vị"))
categories.append(Category("Trứng gà, vịt"))
categories.append(Category("Sữa & Sản phẩm từ sữa"))
categories.append(Category("Khác"))
print("List of Categories: ")
for cate in categories:
    print(cate)
jff=JsonFileFactory()
filename="../dataset/categories.json"
jff.write_data(categories,filename)
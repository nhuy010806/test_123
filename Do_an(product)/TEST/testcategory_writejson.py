from libs.JsonFileFactory import JsonFileFactory
from models.Category import Category

categories=[]
categories.append(Category("Trái cây"))
categories.append(Category("Rau củ"))
categories.append(Category("Khác"))
print("List of Categories: ")
for cate in categories:
    print(cate)
jff=JsonFileFactory()
filename="../dataset/categories.json"
jff.write_data(categories,filename)
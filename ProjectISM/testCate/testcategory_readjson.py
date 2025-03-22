from Category.libs_cate.JsonFileFactory import JsonFileFactory
from Category.models_cate.Category import Category

categories=[]
jff=JsonFileFactory()
filename= "../dataset/categories.json"
categories=jff.read_data(filename,Category)
print("List of Categories after loading Json: ")
for cate in categories:
    print(cate)

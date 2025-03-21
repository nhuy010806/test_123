from DOAN1.libs.JsonFileFactory import JsonFileFactory
from DOAN1.models.Category import Category

categories=[]
jff=JsonFileFactory()
filename="../dataset/categories.json"
categories=jff.read_data(filename,Category)
print("List of categories after read:")
for cate in categories:
    print(cate)

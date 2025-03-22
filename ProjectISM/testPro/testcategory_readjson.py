from libs.JsonFileFactory import JsonFileFactory
from models.Category import Category

categories=[]
jff=JsonFileFactory()
filename="../dataset/categories.json"
categories=jff.read_data(filename,Category)
print("List of Categories after loading Json: ")
for cate in categories:
    print(cate)

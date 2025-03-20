from DOAN1libs.JsonFileFactory import JsonFileFactory
from DOAN1.models.Category import Category

categories=[]
categories.append(Category("Trái cây","Các loại trái cây tươi ngon, giàu vitamin"))
categories.append(Category("Rau củ","Rau xanh và củ quả tươi, giàu dinh dưỡng"))
categories.append(Category("Thực phẩm hữu cơ","Sản phẩm hữu cơ, an toàn và không hóa chất"))
categories.append(Category("Nông sản địa phương","Nông sản được trồng và thu hoạch tại địa phương"))
categories.append(Category("Thảo mộc & Gia vị","Các loại gia vị và thảo mộc tự nhiên"))
categories.append(Category("Trứng gà, vịt","Trứng sạch từ gà và vịt, giàu protein"))
categories.append(Category("Sữa & Sản phẩm từ sữa","Sữa tươi và các sản phẩm từ sữa như phô mai, sữa chua"))
categories.append(Category("Khác"))
print("List of Categories: ")
for cate in categories:
    print(cate)
jff=JsonFileFactory()
filename="../dataset/categories.json"
jff.write_data(categories,filename)
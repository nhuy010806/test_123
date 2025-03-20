from Midterm_NgoThiPhuongThao.libs.JsonFileFactory import JsonFileFactory
from Midterm_NgoThiPhuongThao.models.Product import Product

products=[]
products.append(Product("F1","Cam Sành","100","8.000","10.000","Trái cây"))
products.append(Product("F2","Xoài Tứ Quý","50","15.000","18.000","Trái cây"))
products.append(Product("F3","Táo Envy","50","70.000","110.000","Trái cây"))
products.append(Product("F4","Ổi Hồng","100","20.000","30.000","Trái cây"))
products.append(Product("V1","Cải Thảo","150","10.000","12.000","Rau củ"))
products.append(Product("V2","Khoai Tây","100","11.000","15.000",",Rau củ"))
products.append(Product("V3","Bí Ngô","50","20.000","25.000",",Rau củ"))
products.append(Product("V3","Bí Ngô","50","20.000","25.000",",Rau củ"))
products.append(Product("O1","Hạt Dẻ Cười","50","70.000","100.000","Khác"))
products.append(Product("O2","Hạt Óc Chó","50","90.000","150.000","Khác"))
products.append(Product("O3","Nước Ép Táo","50","6.000","15.000","Khác"))
jff=JsonFileFactory()
filename="../dataset/products.json"
jff.write_data(products,filename)
for p in products:
    print(p)


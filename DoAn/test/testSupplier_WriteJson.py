from DoAn.libs.JsonFileFactory import JsonFileFactory
from DoAn.models.Supplier import Supplier

suppliers = []
suppliers.append(Supplier("SUP1", "Công ty TNHH MTP", "1/1/2024", "cà chua", 5, "5 năm", "ISO 9001", "Đà Lạt","mtp@supplier.com|+84 912 345 678"))
suppliers.append(Supplier("SUP2", "Công ty CP SKY", "2/2/2024", "dưa leo", 2, "10 năm", "HACCP", "Đà Nẵng","sky@supplier.com|+84 976 543 210"))
suppliers.append(Supplier("SUP3", "Công ty TNHH JACK", "3/3/2024", "ớt chuông", 3, "3 năm", "GMP", "Lâm Đồng","jack@supplier.com|+84 988 112 233"))
suppliers.append(Supplier("SUP4", "Công ty CP J97", "4/4/2024", "bông cải", 10, "7 năm", "ISO 22000", "Cần Thơ"," j97@supplier.com|+84 935 667 899"))
suppliers.append(Supplier("SUP5", "Công ty TNHH KICM", "5/5/2024", "cà rốt", 19, "12 năm", "VietGAP", "Hà Nội","kicm@supplier.com|+84 923 445 678"))
suppliers.append(Supplier("SUP6", "Công ty CP MONO", "6/6/2024", "hành lá", 20, "8 năm", "HACCP", "TP.HCM","mono@supplier.com|+84 901 223 334"))
suppliers.append(Supplier("SUP7", "Công ty TNHH SOOBIN", "7/7/2024", "tỏi", 25, "15 năm", "Organic", "Hải Phòng","soobin@supplier.com|+84 987 654 321"))
suppliers.append(Supplier("SUP8", "Công ty CP DOMDOM", "8/8/2024", "rau muống", 29, "6 năm", "ISO 14001", "Bình Thuận","domdom@supplier.com|+84 934 112 778"))
suppliers.append(Supplier("SUP9", "Công ty TNHH HTH", "9/9/2024", "bắp cải", 15, "9 năm", "ISO 22000", "Đà Lạt","hth@supplier.com|+84 966 778 889"))
suppliers.append(Supplier("SUP10", "Công ty CP MCK", "10/10/2024", "ngó sen", 15, "10 năm", "HACCP", "Tiền Giang","mck@supplier.com|+84 977 665 432"))



print("Danh sách nhà cung cấp:")
for s in suppliers:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/suppliers.json"
jff.write_data(suppliers, filename)
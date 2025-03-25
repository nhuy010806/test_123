from libs.JsonFileFactory import JsonFileFactory
from models.Supplier import Supplier

suppliers = []
suppliers.append(Supplier("SUP1", "Công ty TNHH MTP", "2025-03-10", "Cam Sành", "Ngắn hạn", "5 năm", "ISO 9001", "Đà Lạt","mtp@supplier.com|+84 912 345 678"))
suppliers.append(Supplier("SUP2", "Công ty CP SKY", "2025-03-12", "Xoài Tứ Quý", "Dài hạn", "10 năm", "HACCP", "Đà Nẵng","sky@supplier.com|+84 976 543 210"))
suppliers.append(Supplier("SUP3", "Công ty TNHH JACK", "2025-05-20", "Táo Envy", "Theo đơn hàng", "3 năm", "GMP", "Lâm Đồng","jack@supplier.com|+84 988 112 233"))
suppliers.append(Supplier("SUP4", "Công ty CP J97", "2025-04-20", "Ổi Hồng", "Ngắn hạn", "7 năm", "ISO 22000", "Cần Thơ"," j97@supplier.com|+84 935 667 899"))
suppliers.append(Supplier("SUP5", "Công ty TNHH KICM", "2025-04-10", "Cải Thảo", "Ngắn hạn", "12 năm", "VietGAP", "Hà Nội","kicm@supplier.com|+84 923 445 678"))
suppliers.append(Supplier("SUP6", "Công ty CP MONO", "2025-04-15", "Khoai Tây", "Dài hạn", "8 năm", "HACCP", "TP.HCM","mono@supplier.com|+84 901 223 334"))
suppliers.append(Supplier("SUP7", "Công ty TNHH SOOBIN", "2025-03-15", "Bí Ngô", "Theo đơn hàng", "15 năm", "Organic", "Hải Phòng","soobin@supplier.com|+84 987 654 321"))
suppliers.append(Supplier("SUP8", "Công ty CP DOMDOM", "2025-04-20", "Dưa leo", "Theo đơn hàng", "6 năm", "ISO 14001", "Bình Thuận","domdom@supplier.com|+84 934 112 778"))
suppliers.append(Supplier("SUP9", "Công ty TNHH HTH", "2025-06-20", "Hạt Dẻ Cười", "Dài hạn", "9 năm", "ISO 22000", "Đà Lạt","hth@supplier.com|+84 966 778 889"))
suppliers.append(Supplier("SUP10", "Công ty CP MCK", "2025-06-20", "Hạt Óc Chó", "Dài hạn", "10 năm", "HACCP", "Tiền Giang","mck@supplier.com|+84 977 665 432"))



print("Danh sách nhà cung cấp:")
for s in suppliers:
    print(s)

jff = JsonFileFactory()
filename = "../dataset/suppliers.json"
jff.write_data(suppliers, filename)
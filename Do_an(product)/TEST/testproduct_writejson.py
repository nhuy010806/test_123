from libs.JsonFileFactory import JsonFileFactory
from models.Product import Product

products=[]
products.append(Product("F1", "Cam Sành", 8000.0, 100, "Trái cây", "2025-03-10"))  # Sắp hết hạn (còn 9 ngày)
products.append(Product("F2", "Xoài Tứ Quý", 15800.0, 50, "Trái cây", "2025-03-12"))  # Sắp hết hạn (còn 11 ngày)
products.append(Product("F3", "Táo Envy", 70000.0, 20, "Trái cây", "2025-05-20"))  # Sắp hết hàng nhưng còn hạn
products.append(Product("F4", "Ổi Hồng", 20000.0, 100, "Trái cây", "2025-04-20"))  # Bình thường

products.append(Product("V1", "Cải Thảo", 10000.0, 150, "Rau củ", "2025-04-10"))  # Bình thường
products.append(Product("V2", "Khoai Tây", 11000.0, 100, "Rau củ", "2025-04-15"))  # Bình thường
products.append(Product("V3", "Bí Ngô", 20000.0, 10, "Rau củ", "2025-03-15"))  # Vừa sắp hết hàng vừa sắp hết hạn
products.append(Product("V4", "Dưa leo", 25000.0, 100, "Rau củ", "2025-04-20"))  # Bình thường

products.append(Product("O1", "Hạt Dẻ Cười", 70000.0, 50, "Khác", "2025-06-20"))  # Bình thường
products.append(Product("O2", "Hạt Óc Chó", 90000.0, 50, "Khác", "2025-07-20"))  # Bình thường
products.append(Product("O3", "Nước Ép Táo", 6000.0, 50, "Khác", "2025-08-20"))  # Bình thường

# Thêm sản phẩm sắp hết hạn
products.append(Product("F5", "Chuối Tiêu", 12000.0, 120, "Trái cây", "2025-03-05"))  # Sắp hết hạn (còn 4 ngày)
products.append(Product("F6", "Dưa Hấu", 18000.0, 80, "Trái cây", "2025-03-07"))  # Sắp hết hạn (còn 6 ngày)
products.append(Product("F7", "Lê Hàn Quốc", 80000.0, 60, "Trái cây", "2025-03-13"))  # Sắp hết hạn (còn 12 ngày)

# Thêm sản phẩm sắp hết hàng
products.append(Product("F8", "Cam Xoàn", 10000.0, 25, "Trái cây", "2025-06-01"))  # Sắp hết hàng nhưng còn hạn
products.append(Product("F9", "Thanh Long", 15000.0, 18, "Trái cây", "2025-07-10"))  # Sắp hết hàng nhưng còn hạn

# Thêm sản phẩm vừa sắp hết hàng vừa sắp hết hạn
products.append(Product("F10", "Măng Cụt", 90000.0, 12, "Trái cây", "2025-03-08"))  # Vừa sắp hết hàng vừa sắp hết hạn (còn 7 ngày)
products.append(Product("V5", "Cà Rốt", 8000.0, 5, "Rau củ", "2025-03-10"))  # Vừa sắp hết hàng vừa sắp hết hạn (còn 9 ngày)




print("List of Products: ")
for product in products:
    print(product)
jff=JsonFileFactory()
filename="../dataset/products.json"
jff.write_data(products,filename)
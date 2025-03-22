import xml.etree.ElementTree as ET
import pandas as pd

from Category.models_cate.Category import Category
from Product.models_product.Product import Product


class ExportTool:
    # EXCEL
    def export_products_EXCEL(self, filename, products):
        data = {
            "Product ID": [p.proid for p in products],
            "Product Name": [p.proname for p in products],
            "Price": [p.price for p in products],
            "Quantity": [p.quantity for p in products],
            "Cate Name": [p.cateid for p in products],
            "Date": [p.date for p in products],
        }
        df = pd.DataFrame(data)
        df.to_excel(filename, sheet_name="Products", index=False, engine="xlsxwriter")
    def export_categories_EXCEL(self, filename, categories):
        data = {
            "Category Name": [c.cateid for c in categories]
        }
        df = pd.DataFrame(data)
        df.to_excel(filename, sheet_name="Categories", index=False, engine="xlsxwriter")
    def import_products_EXCEL(self, filename):
        df = pd.read_excel(filename, sheet_name=0)
        products = [
            Product(
                row["Product ID"],
                row["Product Name"],
                float(row["Price"]),
                int(row["Quantity"]),
                row["Cate Name"],
                str(row["Date"])
            )
            for _, row in df.iterrows()
        ]
        return products
    def import_categories_EXCEL(self, filename):
        df = pd.read_excel(filename, sheet_name=0)
        categories = [Category(row["Category Name"])
                      for _, row in df.iterrows()]
        return categories

    # TXT:
    def export_products_TXT(self, filename, products):
        df = pd.DataFrame([p.__dict__ for p in products])
        df.to_csv(filename, index=False, sep=",", encoding="utf-8")
    def export_categories_TXT(self, filename, categories):
        df = pd.DataFrame([c.__dict__ for c in categories])
        df.to_csv(filename, index=False, sep=",", encoding="utf-8")
    def import_products_TXT(self, filename):
        df = pd.read_csv(filename, sep=",", encoding="utf-8")
        return [Product(**row) for _, row in df.iterrows()]
    def import_categories_TXT(self, filename):
        df = pd.read_csv(filename, sep=",", encoding="utf-8")
        return [Category(**row) for _, row in df.iterrows()]

    # CSV
    def export_products_CSV(self, filename, products):
        df = pd.DataFrame([p.__dict__ for p in products])
        df.to_csv(filename, index=False, encoding="utf-8")
    def export_categories_CSV(self, filename, categories):
        df = pd.DataFrame([c.__dict__ for c in categories])
        df.to_csv(filename, index=False, encoding="utf-8")
    def import_products_CSV(self, filename):
        df = pd.read_csv(filename, encoding="utf-8")
        return [Product(**row) for _, row in df.iterrows()]
    def import_categories_CSV(self, filename):
        df = pd.read_csv(filename, encoding="utf-8")
        return [Category(**row) for _, row in df.iterrows()]

        # Pickle:
    def export_products_PICKLE(self, filename, products):
        df = pd.DataFrame([p.__dict__ for p in products])
        df.to_pickle(filename)
    def export_categories_PICKLE(self, filename, categories):
        df = pd.DataFrame([c.__dict__ for c in categories])
        df.to_pickle(filename)
    def import_products_PICKLE(self, filename):
        df = pd.read_pickle(filename)
        return [Product(**row) for _, row in df.iterrows()]
    def import_categories_PICKLE(self, filename):
        df = pd.read_pickle(filename)
        return [Category(**row) for _, row in df.iterrows()]

    # JSON
    def export_products_JSON(self, filename, products):
        df = pd.DataFrame([p.__dict__ for p in products])
        df.to_json(filename, orient="records", force_ascii=False, indent=4)
    def export_categories_JSON(self, filename, categories):
        df = pd.DataFrame([c.__dict__ for c in categories])
        df.to_json(filename, orient="records", force_ascii=False, indent=4)
    def import_products_JSON(self, filename):
        df = pd.read_json(filename)
        return [Product(**row) for _, row in df.iterrows()]
    def import_categories_JSON(self, filename):
        df = pd.read_json(filename)
        return [Category(**row) for _, row in df.iterrows()]

        # XML:

    def export_products_XML(self, filename, products):
        root = ET.Element("Products")
        for product in products:
            product_elem = ET.SubElement(root, "Product")
            ET.SubElement(product_elem, "ProductID").text = str(product.proid)
            ET.SubElement(product_elem, "ProductName").text = product.proname
            ET.SubElement(product_elem, "Price").text = str(product.price)
            ET.SubElement(product_elem, "Quantity").text = str(product.quantity)
            ET.SubElement(product_elem, "CategoryID").text = str(product.cateid)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    def export_categories_XML(self, filename, categories):
        root = ET.Element("Categories")
        for category in categories:
            category_elem = ET.SubElement(root, "Category")
            ET.SubElement(category_elem, "CategoryID").text = str(category.cateid)
            ET.SubElement(category_elem, "CategoryName").text = category.catename
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    def import_products_XML(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            products = []
            for product_elem in root.findall("Product"):
                proid = product_elem.find("ProductID").text
                proname = product_elem.find("ProductName").text
                price = float(product_elem.find("Price").text)
                quantity = int(product_elem.find("Quantity").text)
                cateid = product_elem.find("CategoryID").text
                products.append(Product(proid, proname, price, quantity, cateid))
            return products
        except Exception as e:
            print(f"Lỗi khi đọc file XML: {e}")
            return []

    def import_categories_XML(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            categories = []
            for category_elem in root.findall("Category"):
                cateid = category_elem.find("CategoryID").text
                catename = category_elem.find("CategoryName").text
                categories.append(Category(cateid, catename))
            return categories
        except Exception as e:
            print(f"Lỗi khi đọc file XML: {e}")
            return []
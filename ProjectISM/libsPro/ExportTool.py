import pandas as pd

from models.Category import Category
from models.Product import Product


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
            "Category Name": [c if isinstance(c, str) else c.cateid for c in categories]
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






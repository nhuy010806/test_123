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






import os
import webbrowser
import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QMovie
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox, QMainWindow

from libs.JsonFileFactory import JsonFileFactory
from libsPro.DataConnector import DataConnector
from libsPro.ExportTool import ExportTool
from models.Product import Product
from uiPro.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(QMainWindow,Ui_MainWindow):
    def __init__(self,menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.dateEditFilter = None
        self.dc = DataConnector()
        self.categories = self.dc.get_all_cateids()
        self.all_products = self.dc.get_all_products()
        self.original_all_products = self.all_products.copy()
        self.products = self.all_products.copy()
        self.selected_cate = None
        self.is_filtered = False
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.movie = QMovie("../images/backgrproduct.gif")
        self.labelBackground.setMovie(self.movie)
        self.movie.start()
        self.set_buttons_enabled(False)
        self.listWidgetCategory.hide()
        self.show_categories_gui()
        self.products = []
        self.show_products_gui()
        self.is_show_all_clicked = False
        self.setupSignalAndSlot()

    def showWindow(self):
        self.show()

    def show_categories_gui(self):
        self.listWidgetCategory.clear()
        for cate in self.categories:
            cate_item = QListWidgetItem(str(cate))
            cate_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.listWidgetCategory.addItem(cate_item)

    def show_products_gui(self):
        self.tableWidgetProduct.setRowCount(0)
        for product in self.products:
            if not product:
                continue
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            col_proid = QTableWidgetItem(product.proid)
            col_proname = QTableWidgetItem(product.proname)
            col_price = QTableWidgetItem(str(product.price))
            col_quantity = QTableWidgetItem(str(product.quantity))
            col_cateid = QTableWidgetItem(str(product.cateid))
            col_date = QTableWidgetItem(str(product.date))

            self.tableWidgetProduct.setItem(row, 0, col_proid)
            self.tableWidgetProduct.setItem(row, 1, col_proname)
            self.tableWidgetProduct.setItem(row, 2, col_price)
            self.tableWidgetProduct.setItem(row, 3, col_quantity)
            self.tableWidgetProduct.setItem(row, 4, col_cateid)
            self.tableWidgetProduct.setItem(row, 5, col_date)

        self.labelPhoto.setText("")
    def show_all_products(self):
        self.products = self.original_all_products.copy()
        self.is_filtered = False
        self.is_show_all_clicked = True
        self.listWidgetCategory.clearSelection()
        self.listWidgetCategory.show()
        self.show_products_gui()
        self.set_buttons_enabled(True)

    def setupSignalAndSlot(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.filter_product)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.show_detail_product)
        self.pushButtonClear.clicked.connect(self.clear_product_details)
        self.pushButtonSave.clicked.connect(self.save_product)
        self.pushButtonDelete.clicked.connect(self.delete_product)
        self.pushButtonSearch.clicked.connect(self.search_product)
        self.pushButtonFilterDate.clicked.connect(self.toggle_filter_colored_products)
        self.pushButtonShowall.clicked.connect(self.show_all_products)
        self.pushButtonBack.clicked.connect(self.back_program)

        self.exportExcel_file.triggered.connect(self.export_to_excel)
        self.importExcel_file.triggered.connect(self.import_from_excel)
        self.actionHelp_2.triggered.connect(self.open_help)
        self.exportCSV_file.triggered.connect(self.export_to_csv)
        self.importCSV_file.triggered.connect(self.import_from_csv)
        self.exportTXT_file.triggered.connect(self.export_to_txt)
        self.importTXT_file.triggered.connect(self.import_from_txt)
        self.exportJson_file.triggered.connect(self.export_to_json)
        self.importJson_file.triggered.connect(self.import_from_json)

    def set_buttons_enabled(self, enabled):
        self.pushButtonSearch.setEnabled(enabled)
        self.pushButtonFilterDate.setEnabled(enabled)
        self.pushButtonSave.setEnabled(enabled)
        self.pushButtonDelete.setEnabled(enabled)
        self.pushButtonClear.setEnabled(enabled)

    def filter_product(self):
        if not self.is_show_all_clicked:
            return
        row = self.listWidgetCategory.currentRow()
        if row < 0:
            return
        self.selected_cate = self.categories[row]
        self.products = self.dc.get_products_by_categories(self.selected_cate)
        self.show_products_gui()

    def toggle_filter_colored_products(self):
        if not self.is_filtered:
            self.products = self.original_all_products.copy()
        self.products = [p for p in self.original_all_products
                         if p and self.get_product_color(p, datetime.date.today()) is not None]
        self.is_filtered = True
        self.show_products_gui()
        self.update_colored_products()

    def filter_colored_products(self):
        today = datetime.date.today()
        if self.selected_cate:
            all_products = self.dc.get_products_by_categories(self.selected_cate.cateid)
        else:
            all_products = self.dc.get_all_products()
        self.products = [p for p in all_products
                         if p and self.get_product_color(p, today) is not None]
        self.show_products_gui()
        self.update_colored_products()

    def update_colored_products(self):
        today = datetime.date.today()
        count_expiring = 0
        count_low_stock = 0
        count_both = 0
        total_rows = self.tableWidgetProduct.rowCount()
        total_products = len(self.products)
        for row in range(min(total_rows, total_products)):
            product = self.products[row]
            if not product:
                continue
            color = self.get_product_color(product, today)
            if color:
                for col in range(self.tableWidgetProduct.columnCount()):
                    item = self.tableWidgetProduct.item(row, col)
                    if item:
                        item.setBackground(color)
            is_expiring = self.days_until_expiry(product, today) <= 15
            is_low_stock = int(product.quantity) < 30
            if is_expiring and is_low_stock:
                count_both += 1
            elif is_expiring:
                count_expiring += 1
            elif is_low_stock:
                count_low_stock += 1
        summary_text = (f"<p style='line-height: 1.8; text-align: left;'>"
                        f"<b>Sắp hết hạn (vàng):</b> {count_expiring} sản phẩm<br>"
                        f"<b>Sắp hết hàng (xanh):</b> {count_low_stock} sản phẩm<br>"
                        f"<b>Cả hai (đỏ):</b> {count_both} sản phẩm"
                        f"</p>")
        self.labelPhoto.setText(summary_text)

    def days_until_expiry(self, product, today):
        try:
            expiry_date = datetime.datetime.strptime(product.date, "%Y-%m-%d").date()
            return (expiry_date - today).days
        except ValueError:
            return float('inf')

    def get_product_color(self, product, today):
        days_left = self.days_until_expiry(product, today)
        try:
            quantity = int(product.quantity)
        except ValueError:
            return None
        if days_left <= 15 and quantity < 30:
            return QColor(255, 102, 102)  # Đỏ
        elif days_left <= 15:
            return QColor(253, 253, 150)   # Vàng
        elif quantity < 30:
            return QColor(167, 199, 231)  # Xanh da trời
        return None

    def show_detail_product(self):
        index = self.tableWidgetProduct.currentRow()
        if index < 0:
            return
        product = self.products[index]
        self.lineEditProductID.setText(product.proid)
        self.lineEditProductName.setText(product.proname)
        self.lineEditPrice.setText(str(product.price))
        self.lineEditQuantity.setText(str(product.quantity))
        self.lineEditCateID.setText(product.cateid)
        self.lineEditDate.setText(str(product.date))

    def clear_product_details(self):
        self.lineEditProductID.clear()
        self.lineEditProductName.clear()
        self.lineEditPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditCateID.clear()
        self.lineEditDate.clear()
        self.lineEditSearch.clear()
        self.labelPhoto.clear()
        self.restore_previous_product_color()

    def save_product(self):
        proid = self.lineEditProductID.text().strip()
        proname = self.lineEditProductName.text().strip()
        price_text = self.lineEditPrice.text().strip()
        quantity_text = self.lineEditQuantity.text().strip()
        cateid = self.lineEditCateID.text().strip()
        date = self.lineEditDate.text().strip()
        if not (proid and proname and price_text and quantity_text and cateid and date):
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin sản phẩm.")
            return
        try:
            price = float(price_text)
            quantity = int(quantity_text)
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Giá và số lượng phải là số hợp lệ.")
            return
        product = Product(proid, proname, price, quantity, cateid, date)
        index = next((i for i, p in enumerate(self.products) if p.proid == proid), -1)
        if index == -1:
            self.products.append(product)
        else:
            self.products[index] = product
        jff = JsonFileFactory()
        filename = "../dataset/products.json"
        jff.write_data(self.products, filename)
        self.show_products_gui()

    def delete_product(self):
        proid=self.lineEditProductID.text()
        msgbox=QMessageBox(self.MainWindow)
        msgbox.setText("Chắc chắn muốn xóa sản phẩm có ID ["+proid+"] phải không?")
        msgbox.setWindowTitle("Xác nhận xóa")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec()==QMessageBox.StandardButton.No:
            return
        self.dc.delete_product(proid)
        if self.selected_cate==None:
            self.products=self.dc.get_all_products()
        else:
            cateid=self.selected_cate.cateid
            self.products=self.dc.get_products_by_categories(cateid)
        self.show_products_gui()

    def search_product(self):
        search_text = self.lineEditSearch.text().strip().lower()
        if not search_text:
            self.labelPhoto.setText(f"Vui lòng nhập ID hoặc Tên sản phẩm để tìm kiếm.")
            return
        product = next((p for p in self.products if p.proid.lower() == search_text or p.proname.lower() == search_text),None)
        if hasattr(self, 'selected_row') and self.selected_row is not None:
            self.restore_previous_product_color()
        if product:
            info_text = (f"<p style='line-height: 1.5;'>"
                        f"<b>ID:</b> {product.proid}<br>"
                        f"<b>Tên:</b> {product.proname}<br>"
                        f"<b>Giá:</b> {product.price}/kg<br>"
                        f"<b>Số lượng:</b> {product.quantity}kg<br>"
                        f"<b>Danh mục:</b> {product.cateid}<br>"
                        f"<b>Ngày:</b> {product.date}"
                        f"</p>")
            self.labelPhoto.setText(info_text)
            self.labelPhoto.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            for row in range(self.tableWidgetProduct.rowCount()):
                item = self.tableWidgetProduct.item(row, 0)
                if item and (item.text().lower() == product.proid.lower()):
                    self.selected_row = row
                    self.previous_colors = {}
                    for col in range(self.tableWidgetProduct.columnCount()):
                        cell = self.tableWidgetProduct.item(row, col)
                        if cell:
                            self.previous_colors[col] = cell.background()
                            cell.setBackground(QColor("#00806c"))
                    break
        else:
            self.labelPhoto.setText(f"Không tìm thấy sản phẩm có ID hay tên: {search_text}")

    def restore_previous_product_color(self):
        if hasattr(self, 'selected_row') and self.selected_row is not None:
            for col, color in self.previous_colors.items():
                item = self.tableWidgetProduct.item(self.selected_row, col)
                if item:
                    item.setBackground(color)
            self.selected_row = None
            self.previous_colors = {}

    def back_program(self):
        self.menu_window.show()
        self.close()

    def export_to_excel(self):
        filename_product = '../dataset/products.xlsx'
        extool = ExportTool()
        extool.export_products_EXCEL(filename_product, self.products)

        filename_cate = "../dataset/categories.xlsx"
        extool.export_categories_EXCEL(filename_cate, self.categories)

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export excel thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_from_excel(self):
        filename_product = '../dataset/products.xlsx'
        filename_cate = "../dataset/categories.xlsx"
        extool = ExportTool()
        self.categories = extool.import_categories_EXCEL(filename_cate)
        self.products = extool.import_products_EXCEL(filename_product)
        self.show_products_gui()
        self.show_categories_gui()

    # TXT:
    def export_to_txt(self):
        filename_product = "../dataset/products.txt"
        extool = ExportTool()
        extool.export_products_TXT(filename_product, self.products)

        filename_cate = "../dataset/categories.txt"
        extool.export_categories_TXT(filename_cate, self.categories)

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export txt thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_from_txt(self):
        filename_product = '../dataset/products.txt'
        filename_cate = "../dataset/categories.txt"
        extool = ExportTool()
        self.categories = extool.import_categories_TXT(filename_cate)
        self.products = extool.import_products_TXT(filename_product)
        self.show_products_gui()
        self.show_categories_gui()

    # CSV
    def export_to_csv(self):
        filename_product = "../dataset/products.csv"
        extool = ExportTool()
        extool.export_products_CSV(filename_product, self.products)

        filename_cate = "../dataset/categories.csv"
        extool.export_categories_CSV(filename_cate, self.categories)

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export csv thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_from_csv(self):
        filename_product = '../dataset/products.csv'
        filename_cate = "../dataset/categories.csv"
        extool = ExportTool()
        self.categories = extool.import_categories_CSV(filename_cate)
        self.products = extool.import_products_CSV(filename_product)
        self.show_products_gui()
        self.show_categories_gui()

    # # PICKLE
    # def export_to_pickle(self):
    #     filename_product = "../dataset_product/products.pickle"
    #     extool = ExportTool()
    #     extool.export_products_PICKLE(filename_product, self.products)
    #
    #     filename_cate = "../dataset_product/categories.pickle"
    #     extool.export_categories_PICKLE(filename_cate, self.categories)
    #
    #     msgbox = QMessageBox(self.MainWindow)
    #     msgbox.setText("Đã export pickle thành công")
    #     msgbox.setWindowTitle("Thông báo")
    #     msgbox.exec()
    #
    # def import_from_pickle(self):
    #     filename_product = '../dataset_product/products.pickle'
    #     filename_cate = "../dataset_product/categories.pickle"
    #     extool = ExportTool()
    #     self.categories = extool.import_categories_PICKLE(filename_cate)
    #     self.products = extool.import_products_PICKLE(filename_product)
    #     self.show_products_gui()
    #     self.show_categories_gui()

    # XML
    # def export_to_xml(self):
    #     filename_product = "../dataset_product/products.xml"
    #     extool = ExportTool()
    #     extool.export_products_XML(filename_product, self.products)
    #
    #     filename_cate = "../dataset_product/categories.xml"
    #     extool.export_categories_XML(filename_cate, self.categories)
    #
    #     msgbox = QMessageBox(self.MainWindow)
    #     msgbox.setText("Đã export xml thành công")
    #     msgbox.setWindowTitle("Thông báo")
    #     msgbox.exec()
    #
    # def import_from_xml(self):
    #     filename_product = '../dataset_product/products.xml'
    #     filename_cate = "../dataset_product/categories.xml"
    #     extool = ExportTool()
    #     self.categories = extool.import_categories_XML(filename_cate)
    #     self.products = extool.import_products_XML(filename_product)
    #     self.show_products_gui()
    #     self.show_categories_gui()

    # JSON
    def export_to_json(self):
        filename_product = "../dataset/products.json"
        extool = ExportTool()
        extool.export_products_JSON(filename_product, self.products)

        filename_cate = "../dataset/categories.json"
        extool.export_categories_JSON(filename_cate, self.categories)

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export json thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_from_json(self):
        filename_product = '../dataset/products.json'
        filename_cate = "../dataset/categories.json"
        extool = ExportTool()
        self.categories = extool.import_categories_JSON(filename_cate)
        self.products = extool.import_products_JSON(filename_product)
        self.show_products_gui()
        self.show_categories_gui()

    def open_help(self):
        file_help = "HELP PRODUCT.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../help/{file_help}"
        webbrowser.open_new(file_help)
















import os
import webbrowser

from PyQt6.QtGui import QMovie
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox, QMainWindow

from libsCate.DataConnector import DataConnector
from models.Category import Category
from uiCate.CategoryMainWindow import Ui_MainWindow


class ProductMainWindow1Ext(QMainWindow, Ui_MainWindow):
    category_updated = pyqtSignal()
    def __init__(self,menu_window):
        super().__init__()
        self.menu_window=menu_window
        self.dc = DataConnector()
        #self.categories = self.dc.get_all_categories()  # Load danh sách Cate ID và description
        self.categories = []
        self.selected_cate = None
        self.setupUi(self)
        #self.product_window = product_window


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_categories_gui()
        self.setupSignalAndSlot()
        self.movie = QMovie("../images/FARMERS1.gif")
        self.labelBackground.setMovie(self.movie)
        self.movie.start()
        self.set_buttons_enabled(False)

    def showWindow(self):
        self.show()

    def show_categories_gui(self):
        self.listWidgetCategory.clear()
        for cate in self.categories:
            cate_item = QListWidgetItem(str(cate.cateid))
            self.listWidgetCategory.addItem(cate_item)

    def setupSignalAndSlot(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.filter_category)
        self.pushButtonSave.clicked.connect(self.save_category)
        self.pushButtonDelete.clicked.connect(self.delete_category)
        self.pushButtonShowall.clicked.connect(self.show_all_category)
        self.actionCurrentHelp.triggered.connect(self.open_help)
        self.pushButtonBack.clicked.connect(self.back_window)
        self.pushButtonClear.clicked.connect(self.clear_cate_details)

    def set_buttons_enabled(self, enabled: bool):

        self.pushButtonSave.setEnabled(enabled)
        self.pushButtonDelete.setEnabled(enabled)
        self.pushButtonClear.setEnabled(enabled)

    def filter_category(self):
        row = self.listWidgetCategory.currentRow()
        if row < 0 or row >= len(self.categories):
            return
        self.selected_cate = self.categories[row]
        self.lineEditCateID.setText(self.selected_cate.cateid)
        self.lineEditDescription.setText(self.selected_cate.description)

    def save_category(self):
        cateid = self.lineEditCateID.text().strip()
        description = self.lineEditDescription.text().strip() # Lấy description từ LineEdit
        if not cateid:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập Cate ID!")
            return
        category = Category(cateid, description)
        index = self.dc.find_index_category(category.cateid)
        if index == -1:
            self.dc.save_newcategory(category)
        else:
            self.dc.save_update_category(category)

        self.categories = self.dc.get_all_categories()
        self.show_categories_gui()
        self.category_updated.emit()
        # if self.product_window:
        #     self.product_window.save_update_category(category)


    def delete_category(self):
        cateid = self.lineEditCateID.text().strip()
        if not cateid:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một Cate ID để xóa!")
            return

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText(f"Bạn có chắc muốn xóa [{cateid}] ?")
        msgbox.setWindowTitle("Xác nhận xóa!")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)

        if msgbox.exec() == QMessageBox.StandardButton.No:
            return

        self.dc.delete_category(cateid)
        self.categories = self.dc.get_all_categories()
        self.show_categories_gui()
        self.lineEditCateID.clear()
        self.lineEditDescription.clear()

    def show_all_category(self):
        self.categories = self.dc.get_all_categories()

        if not self.categories:
            QMessageBox.information(
                self.MainWindow,
                "Thông báo",
                " Hiện không có danh mục nào trong hệ thống."
            )
            return
        self.show_categories_gui()
        self.set_buttons_enabled(True)

    def open_help(self):
        file_help = "Hướng dẫn sử dụng category.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../asset/{file_help}"
        webbrowser.open_new(file_help)
    def back_window(self):
        self.MainWindow.close()
        self.menu_window.show()

    def clear_cate_details(self):
        self.lineEditCateID.clear()
        self.lineEditDescription.clear()

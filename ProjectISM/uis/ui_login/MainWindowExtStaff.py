from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import Qt
from staff.CategoryMainWindowExtStaff import CategoryMainWindowExtStaff
from staff.MainWindowDoAnExtStaff import MainWindowDoAnExtStaff
from staff.ProductMainWindowExtStaff import ProductMainWindowExtStaff
from uis.ui_login.MainWindowMenu import Ui_MainWindow


class MainWindowMenuExtStaff( QMainWindow, Ui_MainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.movie = QMovie("../images/menubackground.gif")
        self.labelBackground.setMovie(self.movie)
        self.movie.start()

    def setupSignalAndSlot(self):
       # self.pushButtonEmployee.clicked.connect(self.xuli_nhanvien)
       self.pushButtonEmployee.setEnabled(False)
       self.pushButtonEmployee.setFocusPolicy(Qt.FocusPolicy.NoFocus)
       self.pushButtonEmployee.setStyleSheet("""
           QPushButton {
               background-color: #aaaaaa !important;
               color: #ffffff !important;
               border: 1px solid #888888 !important;
               border-radius: 15px;
               font: bold 12pt "Tahoma";
           }
           QPushButton:hover, QPushButton:focus {
               background-color: #aaaaaa !important;
               color: #ffffff !important;
           }
       """)

       self.pushButtonSupplier.clicked.connect(self.xuli_supplier)
       self.pushButtonProduct.clicked.connect(self.xuly_product)
       self.pushButtonCategory.clicked.connect(self.xuly_category)
    # def xuli_nhanvien(self):
    #     self.employee_window = MainWindowEmployeeExt(self)
    #     self.employee_window.show()
    #     self.close()
    def xuli_supplier(self):
        self.supplier_window=MainWindowDoAnExtStaff(self)
        self.supplier_window.show()
        self.close()
    def xuly_product(self):
        self.product_window=ProductMainWindowExtStaff(self)
        self.product_window.show()
        self.close()
    def xuly_category(self):
        self.product_category = CategoryMainWindowExtStaff(self)
        self.product_category.show()
        self.close()




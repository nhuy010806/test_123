from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QMainWindow

from uiCate.CategoryMainWindowExt import ProductMainWindow1Ext
from uiPro.ProductMainWindowExt import ProductMainWindowExt
from uiSup.MainWindowDoAnExt import MainWindowDoAnExt
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
        self.pushButtonSupplier.clicked.connect(self.xuli_supplier)
        self.pushButtonProduct.clicked.connect(self.xuly_product)
        self.pushButtonCategory.clicked.connect(self.xuly_category)
    # def xuli_nhanvien(self):
    #     self.employee_window = MainWindowEmployeeExt(self)
    #     self.employee_window.show()
    #     self.close()
    def xuli_supplier(self):
        self.supplier_window=MainWindowDoAnExt(self)
        self.supplier_window.show()
        self.close()
    def xuly_product(self):
        self.product_window=ProductMainWindowExt(self)
        self.product_window.show()
        self.close()
    def xuly_category(self):
        self.product_category = ProductMainWindow1Ext(self)
        self.product_category.show()
        self.close()




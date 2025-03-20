from PyQt6.QtWidgets import QMainWindow
from Midterm_NgoThiPhuongThao.ui.ProductMainWindow import Ui_MainWindow

class ProductMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showWindow(self):  # Phương thức này giúp mở màn hình
        self.show()

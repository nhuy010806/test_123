from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Midterm_NgoThiPhuongThao.ui.Manhinhtrunggian import Ui_MainWindow
from Midterm_NgoThiPhuongThao.ui.ProductMainWindowExt import ProductMainWindowExt

class Manhinhtrunggian(QMainWindow, Ui_MainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window  # Giữ tham chiếu đến màn hình đăng nhập
        self.setupUi(self)
        self.setupSignalsAndSlots()

    def setupSignalsAndSlots(self):
        self.pushButtonNo.clicked.connect(self.xuly_thoat_to_login)
        self.pushButtonYes.clicked.connect(self.xuly_chuyen_sang_product)

    def xuly_thoat_to_login(self):
        msgbox = QMessageBox(self)
        msgbox.setText("Bạn có muốn quay lại màn hình đăng nhập?")
        msgbox.setWindowTitle("Xác nhận")
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            self.login_window.show()  # Hiện lại màn hình đăng nhập
            self.close()  # Đóng màn hình chính
    def xuly_chuyen_sang_product(self):
        self.product_window = ProductMainWindowExt()  # Tạo màn hình Product
        self.product_window.show()
        self.close()

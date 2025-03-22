from PyQt6.QtWidgets import QMainWindow

from uiSup.MainWindowDoAnExt import MainWindowDoAnExt
from uis.ui_employee.MainWindowEmployeeExt import MainWindowEmployeeExt
from uis.ui_login.MainWindowMenu import Ui_MainWindow


class MainWindowMenuExt( QMainWindow, Ui_MainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window  # Giữ tham chiếu đến màn hình đăng nhập
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonEmployee.clicked.connect(self.xuli_nhanvien)
        self.pushButtonSupplier.clicked.connect(self.xuli_supplier)

    def xuli_nhanvien(self):
        self.employee_window = MainWindowEmployeeExt(self)
        self.employee_window.show()
        self.close()  # Đóng cửa sổ Menu sau khi mở Employee
    def xuli_supplier(self):
        self.supplier_window=MainWindowDoAnExt(self)
        self.supplier_window.show()
        self.close()




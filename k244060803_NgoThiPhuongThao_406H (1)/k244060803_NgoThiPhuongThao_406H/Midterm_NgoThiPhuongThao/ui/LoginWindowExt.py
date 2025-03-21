from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Midterm_NgoThiPhuongThao.libs.DataConnector import DataConnector
from Midterm_NgoThiPhuongThao.ui.LoginWindow import Ui_MainWindow
from Midterm_NgoThiPhuongThao.ui.ManhinhtrunggianExt import Manhinhtrunggian

class LoginWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.xuly_login)
        self.pushButtonExit.clicked.connect(self.exit_program)

    def xuly_login(self):
        dc = DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)

        if emp is not None:
            self.mainwindow = Manhinhtrunggian(self)  # Truyền self vào để quay lại sau này
            self.mainwindow.show()
            self.close()  # Đóng màn hình đăng nhập
        else:
            self.msg = QMessageBox(self)
            self.msg.setText("Đăng nhập thất bại!")
            self.msg.exec()

    def exit_program(self):
        msgbox = QMessageBox(self)
        msgbox.setText("Bạn có muốn thoát chương trình?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            self.close()

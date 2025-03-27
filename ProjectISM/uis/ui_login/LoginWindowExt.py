from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from libs.DataConnector import DataConnector
from uis.ui_login.LoginWindow import Ui_MainWindow

from uis.ui_login.MainWindowMenuExt import MainWindowMenuExt


class LoginWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.movie = QMovie("../images/loginbackground.gif")
        self.labelBackground.setMovie(self.movie)
        self.movie.start()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.xuly_login)
        self.pushButtonExit.clicked.connect(self.exit_program)

    def xuly_login(self):
        dc = DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()

        if self.AdminRadio.isChecked()==True:
            emp = dc.login2(uid, pwd)
            if emp is not None:
                self.mainwindow = MainWindowMenuExt(self)  # Truyền self vào để quay lại sau này
                self.mainwindow.show()
                self.close()  # Đóng màn hình đăng nhập
            else:
                self.msg = QMessageBox(self)
                self.msg.setText("Đăng nhập thất bại!")
                self.msg.exec()
        if self.StaffRadio.isChecked() == True:
            emp = dc.login1(uid, pwd)
            if emp is not None:
                self.mainwindow = MainWindowMenuExt(self)  # Truyền self vào để quay lại sau này
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

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from libs.DataConnector import DataConnector
from ui.MainWindowLogin import Ui_MainWindow
from ui.MainWindowMenuExt import MainWindowMenuExt


class MainWindowLoginExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.xuli_login)
    def xuli_login(self):
        dc = DataConnector()
        uid = self.lineEditUsername.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)
        if emp != None:
            self.MainWindow.close()  # close login window
            self.mainwindow = QMainWindow()
            self.myui = MainWindowMenuExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()



from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Midterm_NgoThiPhuongThao.libs.DataConnector import DataConnector
from Midterm_NgoThiPhuongThao.ui.LoginMainWindow import Ui_MainWindow
from Midterm_NgoThiPhuongThao.ui.ManhinhtrunggianExt import manhinhtrunggian


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()


    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.xuly_login)
        self.pushButtonExit.clicked.connect(self.exit_program)
        self.checkBoxSinhVien.clicked.connect(self.xuly_student)
        # self.radioButtontea.clicked.connect(self.xuly_teacher)
        # self.radioButtonlibra.clicked.connect(self.xuly_librarian)

    def xuly_login(self):
        dc = DataConnector()
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)

        if emp is not None:

            user_name = emp.name


            if self.checkBoxSinhVien.isChecked():
                role = "Sinh Viên"
            elif self.checkBoxGiangVien.isChecked():
                role = "Giảng Viên"
            elif self.checkBoxThuThu.isChecked():
                role = "Thủ Thư"

            if emp != None:
                self.MainWindow.close()
                self.mainwindow = QMainWindow()
                self.myui = manhinhtrunggian()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                self.msg = QMessageBox(self.MainWindow)
                self.msg.setText("Đăng nhập thất bại!")
                self.msg.exec()
    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("e mun thoat phan mem nay ha")
        msgbox.setWindowTitle("xac nhan thoat")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()
    def xuly_student(self):
        pass




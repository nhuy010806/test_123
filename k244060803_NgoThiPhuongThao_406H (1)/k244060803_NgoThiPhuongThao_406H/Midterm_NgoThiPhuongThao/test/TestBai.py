from PyQt6.QtWidgets import QApplication
from Midterm_NgoThiPhuongThao.ui.LoginWindowExt import LoginWindowExt

app = QApplication([])
myui = LoginWindowExt()
myui.show()
app.exec()

from PyQt6.QtWidgets import QApplication

from uis.ui_login.LoginWindowExt import LoginWindowExt

app = QApplication([])
myui = LoginWindowExt()
myui.show()
app.exec()

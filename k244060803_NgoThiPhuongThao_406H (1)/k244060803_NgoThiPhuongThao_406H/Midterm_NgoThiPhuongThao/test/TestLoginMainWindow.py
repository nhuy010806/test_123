from PyQt6.QtWidgets import QApplication, QMainWindow

from Midterm_NgoThiPhuongThao.ui.LoginWindowExt import LoginMainWindowExt
from Midterm_NgoThiPhuongThao.ui.ManhinhtrunggianExt import manhinhtrunggian

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
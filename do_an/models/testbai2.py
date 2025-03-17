from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowEmployeeExt2 import MainWindowEmployeeExt2

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEmployeeExt2()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
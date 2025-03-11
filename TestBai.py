from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowEmployeeExt import MainWindowEmployeeExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEmployeeExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
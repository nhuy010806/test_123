from PyQt6.QtWidgets import QMainWindow,QApplication
from DOAN1.ui.ProductMainWindowExt import ProductMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ProductMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
from PyQt6.QtWidgets import QApplication, QMainWindow

from uis.uiPro.ProductMainWindowExt import ProductMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=ProductMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
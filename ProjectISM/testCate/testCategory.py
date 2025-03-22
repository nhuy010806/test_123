from PyQt6.QtWidgets import QMainWindow,QApplication

from Category.ui_cate.CategoryMainWindowExt import ProductMainWindow1Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=ProductMainWindow1Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowLoginExt import MainWindowLoginExt
app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowLoginExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()

from PyQt6.QtWidgets import QApplication, QMainWindow

from uis.uiSup.MainWindowSupExt import MainWindowDoAnExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowDoAnExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
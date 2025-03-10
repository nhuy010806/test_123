from libs.DataConnector import DataConnector
from ui.MainWindowMenu import Ui_MainWindow


class MainWindowMenuExt(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.admins=self.dc.get_all_admins()
        self.selected_admins=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def showWindow(self):
        self.MainWindow.show()
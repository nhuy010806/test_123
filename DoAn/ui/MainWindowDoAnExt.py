from email import message

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QTextEdit
from DoAn.libs.DataConnector import DataConnector
from DoAn.libs.ExportTools import ExportTool
from DoAn.models.Supplier import Supplier
from DoAn.ui.MainWindowDoAn import Ui_MainWindow


class MainWindowDoAnExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.selected_cate = None
        self.suppliers = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_supplier_gui()
        self.suppliers = self.dc.get_all_suppliers()
        self.setupSignalAndSlot()

        self.textEditDescription = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEditDescription.setGeometry(QtCore.QRect(30, 320, 231, 81))
        self.textEditDescription.setObjectName("textEditDescription")

    def showWindow(self):
        self.MainWindow.show()

    def show_supplier_gui(self):
        self.tableWidgetSupplier.setRowCount(0)
        for suppliers in self.suppliers:
            row = self.tableWidgetSupplier.rowCount()
            self.tableWidgetSupplier.insertRow(row)

            col_supid = QTableWidgetItem(suppliers.id)
            col_suppname = QTableWidgetItem(suppliers.ten)
            col_supday = QTableWidgetItem(suppliers.ngaynhaphang)
            col_suptensp = QTableWidgetItem(suppliers.tensanpham)
            col_supsoluong = QTableWidgetItem(suppliers.soluong)


            self.tableWidgetSupplier.setItem(row, 0, col_supid)
            self.tableWidgetSupplier.setItem(row, 1, col_suppname)
            self.tableWidgetSupplier.setItem(row, 2, col_supday)
            self.tableWidgetSupplier.setItem(row, 3, col_suptensp)
            self.tableWidgetSupplier.setItem(row, 4, col_supsoluong)

    def setupSignalAndSlot(self):
        self.pushButtonShowAll.clicked.connect(self.show_all_products)
        self.tableWidgetSupplier.itemSelectionChanged.connect(self.show_detail_supplier)
        self.pushButtonSearch.clicked.connect(self.search_supplier)
        self.pushButtonUpdate.clicked.connect(self.xuly_capnhat)
        self.pushButtonSave.clicked.connect(self.save_supplier)
        self.pushButtonClear.clicked.connect(self.clear_supplier_detail)
        self.pushButtonDelete.clicked.connect(self.xuly_xoa)
        self.actionexcel_file.triggered.connect(self.import_to_excel)
        self.actionexcel_file_2.triggered.connect(self.export_to_excel)
        self.pushButtonBack.clicked.connect(self.xuly_quayve)

    def show_all_products(self):
        self.suppliers = self.dc.get_all_suppliers()
        self.show_supplier_gui()

    def show_detail_supplier(self):
        index=self.tableWidgetSupplier.currentRow()
        if index<0:
            return
        supplier=self.suppliers[index]
        self.lineEditSupplierID.setText(supplier.id)
        self.lineEditSupplierName.setText(supplier.ten)
        self.lineEditSupplydate.setText(str(supplier.ngaynhaphang))
        self.lineEditProductname.setText(supplier.tensanpham)
        self.lineEditQuantity.setText(str(supplier.soluong))

        description = (
            f"Thời gian hợp tác: {supplier.thoigian_hoptac}\n"
            
            f"Chứng nhận chất lượng: {supplier.chung_nhan}\n"
            
            f"Nguồn gốc sản phẩm: {supplier.nguon_goc}\n"
            
            f"Thông tin liên lạc: {supplier.thongtin_lienlac}"
        )
        self.textEditDescription.setText(description)

    def clear_supplier_detail(self):
        self.lineEditSupplierID.setText("")
        self.lineEditSupplierName.setText("")
        self.lineEditSupplydate.setText("")
        self.lineEditProductname.setText("")
        self.lineEditQuantity.setText("")
        self.textEditDescription.setText("")

        for row in range(self.tableWidgetSupplier.rowCount()):
            for col in range(self.tableWidgetSupplier.columnCount()):
                if self.tableWidgetSupplier.item(row, col): 
                    self.tableWidgetSupplier.item(row, col).setBackground(QColor(255, 255, 255))

    def show_employee_gui(self):
        self.tableWidgetSupplier.setRowCount(0)
        for supplier in self.suppliers:
            row = self.tableWidgetSupplier.rowCount()
            self.tableWidgetSupplier.insertRow(row)

            col_id = QTableWidgetItem(supplier.id)
            col_ten = QTableWidgetItem(supplier.ten)
            col_ngaynhaphang = QTableWidgetItem(str(supplier.ngaynhaphang))
            col_tensanpham = QTableWidgetItem(supplier.tensanpham)
            col_soluong = QTableWidgetItem(int(supplier.soluong))

            self.tableWidgetSupplier.setItem(row, 0, col_id)
            self.tableWidgetSupplier.setItem(row, 1, col_ten)
            self.tableWidgetSupplier.setItem(row, 2, col_ngaynhaphang)
            self.tableWidgetSupplier.setItem(row, 3, col_tensanpham)
            self.tableWidgetSupplier.setItem(row, 4, col_soluong)


    def xuly_xoa(self):
        index = self.tableWidgetSupplier.currentRow()
        if index < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một nhà cung cấp để xoá!")
            return

        id = self.lineEditSupplierID.text()
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText(f"Bạn muốn xoá nhà cung cấp [{id}] này phải không?")
        msgbox.setWindowTitle("Xác nhận xoá")
        msgbox.setIcon(QMessageBox.Icon.Warning)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.No:
            return

        del self.suppliers[index]
        self.dc.delete_supplier(id)
        self.tableWidgetSupplier.removeRow(index)
        self.lineEditSupplierID.clear()
        self.lineEditSupplierName.clear()
        self.lineEditSupplydate.clear()
        self.lineEditProductname.clear()
        self.lineEditQuantity.clear()

        QMessageBox.information(self.MainWindow, "Thông báo", f"Đã xoá nhà cung cấp [{id}] thành công!")

    def export_to_excel(self):
        filename = '../dataset/suppliers.xlsx'
        extool = ExportTool()
        extool.export_employee_to_excel(filename, self.suppliers)
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export excel thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_to_excel(self):
        filename_cate = "../dataset/suppliers.xlsx"
        extool = ExportTool()
        self.suppliers = extool.import_employee_excel(filename_cate)
        self.show_employee_gui()

    def xuly_quayve(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn muốn quay về trang trước đó?")
        msgbox.setWindowTitle("Xác nhận")
        msgbox.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            print("Quay về")
    def xuly_capnhat(self):
        index = self.tableWidgetSupplier.currentRow()
        if index < 0:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một nhà cung cấp để cập nhật!")
            return

        # Lấy dữ liệu từ QLineEdit
        id = self.lineEditSupplierID.text()
        ten = self.lineEditSupplierName.text()
        ngaynhaphang = self.lineEditSupplydate.text()
        tensanpham = self.lineEditProductname.text()
        soluong = self.lineEditQuantity.text()

        # Cập nhật vào QTableWidget
        self.tableWidgetSupplier.setItem(index, 0, QTableWidgetItem(id))
        self.tableWidgetSupplier.setItem(index, 1, QTableWidgetItem(ten))
        self.tableWidgetSupplier.setItem(index, 2, QTableWidgetItem(ngaynhaphang))
        self.tableWidgetSupplier.setItem(index, 3, QTableWidgetItem(tensanpham))
        self.tableWidgetSupplier.setItem(index, 4, QTableWidgetItem(soluong))

        QMessageBox.information(self.MainWindow, "Thông báo", "Cập nhật thành công!")

    def save_supplier(self):
        print("🔹 Bắt đầu lưu nhà cung cấp...")

        id = self.lineEditSupplierID.text().strip()
        ten = self.lineEditSupplierName.text().strip()
        ngaynhaphang = self.lineEditSupplydate.text().strip()
        tensanpham = self.lineEditProductname.text().strip()
        soluong = self.lineEditQuantity.text().strip()
        if not all([id, ten, ngaynhaphang, tensanpham, soluong]):
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin của nhà cung cấp.")
            return
        try:
            id = str(id)
            soluong = str(soluong)
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "ID nhà cung cấp hoặc số lượng không hợp lệ.")
            return
        supplier = Supplier(id, ten, ngaynhaphang, tensanpham, soluong)

        index = self.dc.find_index_supplier(supplier.id)
        if index == -1:
            self.dc.save_new_supplier(supplier)
        else:
            self.dc.save_update_supplier(supplier)


        self.suppliers = self.dc.get_all_suppliers()
        self.show_supplier_gui()
        message = f"Đã lưu nhà cung cấp: {supplier.ten} (ID: {supplier.id})"
        QMessageBox.information(self.MainWindow, "Thành công", message)

    def search_supplier(self):
        search_id = self.lineEditSearch.text().strip()
        if not search_id:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập Supplier ID để tìm kiếm.")
            return

        supplier = next((s for s in self.suppliers if s.id == search_id), None)

        if supplier:
            self.lineEditSupplierID.setText(supplier.id)
            self.lineEditSupplierName.setText(supplier.ten)
            self.lineEditSupplydate.setText(str(supplier.ngaynhaphang))
            self.lineEditProductname.setText(supplier.tensanpham)
            self.lineEditQuantity.setText(str(supplier.soluong))

        description = (
            f"Thời gian hợp tác: {supplier.thoigian_hoptac}\n"
            
            f"Chứng nhận chất lượng: {supplier.chung_nhan}\n"
            
            f"Nguồn gốc sản phẩm: {supplier.nguon_goc}\n"
            
            f"Thông tin liên lạc: {supplier.thongtin_lienlac}"
        )
        self.textEditDescription.setText(description)

        for row in range(self.tableWidgetSupplier.rowCount()):
            if self.tableWidgetSupplier.item(row, 0).text() == search_id:
                for col in range(self.tableWidgetSupplier.columnCount()):
                    self.tableWidgetSupplier.item(row, col).setBackground(QColor(255, 255, 0))
                break

        else:
            QMessageBox.warning(self.MainWindow, "Không tìm thấy", f"Không tìm thấy nhà cung cấp có ID: {search_id}")





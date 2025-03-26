import os
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QMovie
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from libsSup.DataConnector import DataConnector
from libsSup.ExportTools import ExportTool
from models.Supplier import Supplier
from uiSup.MainWindowDoAn import Ui_MainWindow


class MainWindowDoAnExt(QMainWindow, Ui_MainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.setupUi(self)
    #     self.dc = DataConnector()
    #     self.suppliers = self.dc.get_all_suppliers()
    #     self.setupUi(self)
    #     self.setupSignalAndSlot()
    #     self.selected_cate = None
    #     self.suppliers = []
    #
    # def setupUi(self, MainWindow):
    #     super().setupUi(MainWindow)
    #     self.MainWindow = MainWindow
    #     self.show_supplier_gui()
    #     self.setupSignalAndSlot()
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.dc = DataConnector()
        self.suppliers = self.dc.get_all_suppliers()
        self.setupUi(self)
        self.setupSignalAndSlot()
        self.is_deleting=False
        self.is_updating=False

    def showWindow(self):
        self.show()  # Show self instead of self.MainWindow

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.movie = QMovie("../images/supplierbackground.gif")
        self.labelBackground.setMovie(self.movie)
        self.movie.start()
        self.show_supplier_gui()
       # self.setupSignalAndSlot()
        self.tableWidgetSupplier.setRowCount(0)

    # def showWindow(self):
    #     self.MainWindow.show()

    def show_supplier_gui(self):
        self.tableWidgetSupplier.setRowCount(0)
        for supplier in self.suppliers:
            row = self.tableWidgetSupplier.rowCount()
            self.tableWidgetSupplier.insertRow(row)

            col_supid = QTableWidgetItem(supplier.id)
            col_suppname = QTableWidgetItem(supplier.ten)
            col_supday = QTableWidgetItem(str(supplier.ngaynhaphang))
            col_suptensp = QTableWidgetItem(supplier.tensanpham)
            col_supsoluong = QTableWidgetItem(str(supplier.soluong))

            self.tableWidgetSupplier.setItem(row, 0, col_supid)
            self.tableWidgetSupplier.setItem(row, 1, col_suppname)
            self.tableWidgetSupplier.setItem(row, 2, col_supday)
            self.tableWidgetSupplier.setItem(row, 3, col_suptensp)
            self.tableWidgetSupplier.setItem(row, 4, col_supsoluong)

            self.tableWidgetSupplier.resizeColumnsToContents()
            self.tableWidgetSupplier.resizeRowsToContents()

    def setupSignalAndSlot(self):
        self.pushButtonShowAll.clicked.connect(self.show_all_suppliers)
        self.tableWidgetSupplier.itemSelectionChanged.connect(self.show_detail_supplier)
        self.pushButtonSearch.clicked.connect(self.search_supplier)
        self.pushButtonUpdate.clicked.connect(self.xuly_cap_nhat)
        self.pushButtonSave.clicked.connect(self.save_supplier)
        self.pushButtonClear.clicked.connect(self. clear_product_detail)
        self.pushButtonDelete.clicked.connect(self.xuly_xoa)
        self.actionImport_Excel.triggered.connect(self.import_to_excel)
        self.actionExport_Excel.triggered.connect(self.export_to_excel)
        self.pushButtonBack.clicked.connect(self.xuly_quayve)
        self.actionCurrent_Help.triggered.connect(self.open_help)
        self.tableWidgetSupplier.itemSelectionChanged.connect(self.show_detail_supplier)


        self.lineEditSupplierName.textChanged.connect(self.toggle_clear_button)
        self.lineEditQuantity.textChanged.connect(self.toggle_clear_button)
        self.lineEditSupplydate.textChanged.connect(self.toggle_clear_button)
        self.lineEditSupplierID.textChanged.connect(self.toggle_clear_button)
        self.lineEditProductname.textChanged.connect(self.toggle_clear_button)
        self.toggle_clear_button()

    def show_detail_supplier(self):
        index = self.tableWidgetSupplier.currentRow()
        if index < 0:
            return
        product = self.suppliers[index]
        self.lineEditSupplierID.setText(product.id)
        self.lineEditSupplierName.setText(product.ten)
        self.lineEditSupplydate.setText(product.ngaynhaphang)
        self.lineEditQuantity.setText(str(product.soluong))
        self.lineEditProductname.setText(product.tensanpham)
        for i in range(self.tableWidgetSupplier.rowCount()):
            for j in range(self.tableWidgetSupplier.columnCount()):
                if self.tableWidgetSupplier.item(i, j):
                    self.tableWidgetSupplier.item(i, j).setBackground(QColor(Qt.GlobalColor.white))
        pastel_color = QColor("#FFFACD")
        for j in range(self.tableWidgetSupplier.columnCount()):
            if self.tableWidgetSupplier.item(index, j):
                self.tableWidgetSupplier.item(index, j).setBackground(pastel_color)

    def show_all_suppliers(self):
        self.suppliers = self.dc.get_all_suppliers()
        self.show_supplier_gui()

    # def show_detail_supplier(self):
    #     index=self.tableWidgetSupplier.currentRow()
    #     if index<0:
    #         return
    #     supplier=self.suppliers[index]
    #     self.lineEditSupplierID.setText(supplier.id)
    #     self.lineEditSupplierName.setText(supplier.ten)
    #     self.lineEditSupplydate.setText(str(supplier.ngaynhaphang))
    #     self.lineEditProductname.setText(supplier.tensanpham)
    #     self.lineEditQuantity.setText(str(supplier.soluong))
    #
    #     description = (
    #         f"Thời gian hợp tác: {supplier.thoigian_hoptac}\n"
    #
    #         f"Chứng nhận chất lượng: {supplier.chung_nhan}\n"
    #
    #         f"Nguồn gốc sản phẩm: {supplier.nguon_goc}\n"
    #
    #         f"Thông tin liên lạc: {supplier.thongtin_lienlac}"
    #     )
    #     self.textEditDescription.setText(description)

    # def clear_supplier_detail(self):
    #     self.lineEditSupplierID.setText("")
    #     self.lineEditSupplierName.setText("")
    #     self.lineEditSupplydate.setText("")
    #     self.lineEditProductname.setText("")
    #     self.lineEditQuantity.setText("")
    #     self.textEditDescription.setText("")
    #
    #     for row in range(self.tableWidgetSupplier.rowCount()):
    #         for col in range(self.tableWidgetSupplier.columnCount()):
    #             if self.tableWidgetSupplier.item(row, col):
    #                 self.tableWidgetSupplier.item(row, col).setBackground(QColor(255, 255, 255))


    # def xuly_xoa(self):
    #     index = self.tableWidgetSupplier.currentRow()
    #     if index < 0:
    #         QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một nhà cung cấp để xoá!")
    #         return
    #
    #     id = self.lineEditSupplierID.text()
    #     msgbox = QMessageBox(self.MainWindow)
    #     msgbox.setText(f"Bạn muốn xoá nhà cung cấp [{id}] này phải không?")
    #     msgbox.setWindowTitle("Xác nhận xoá")
    #     msgbox.setIcon(QMessageBox.Icon.Warning)
    #     buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
    #     msgbox.setStandardButtons(buttons)
    #     if msgbox.exec() == QMessageBox.StandardButton.No:
    #         return
    #
    #     del self.suppliers[index]
    #     self.dc.delete_supplier(id)
    #     self.tableWidgetSupplier.removeRow(index)
    #     self.lineEditSupplierID.clear()
    #     self.lineEditSupplierName.clear()
    #     self.lineEditSupplydate.clear()
    #     self.lineEditProductname.clear()
    #     self.lineEditQuantity.clear()
    #
    #
    #     QMessageBox.information(self.MainWindow, "Thông báo", f"Đã xoá nhà cung cấp [{id}] thành công!")
    def xuly_xoa(self):
        if self.is_deleting:
            return

        self.is_deleting = True
        empid = self.lineEditSupplierID.text().strip()
        if not empid:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập ID nhà cung cấp cần xóa!")
            self.is_deleting = False
            return
        msgbox = QMessageBox.question(self, "Xác nhận xóa",
                                      f"Bạn có chắc muốn xóa nhà cung cấp [{empid}] không?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if msgbox == QMessageBox.StandardButton.No:
            self.is_deleting = False
            return

        self.dc.delete_supplier(empid)
        self.suppliers = self.dc.get_all_suppliers()
        self.show_supplier_gui()

        QMessageBox.information(self, "Thành công", "Nhân viên đã được xóa!")
        self.is_deleting = False
    def export_to_excel(self):
        filename = '../dataset/suppliers.xlsx'
        extool = ExportTool()
        extool.export_supplier_to_excel(filename, self.suppliers)
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export excel thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()

    def import_to_excel(self):
        filename_cate = "../dataset/suppliers.xlsx"
        extool = ExportTool()
        self.suppliers = extool.import_supplier_excel(filename_cate)
        self.show_supplier_gui()

    def xuly_quayve(self):
        self.menu_window.show()
        self.close()
    # def xuly_capnhat(self):
    #     index = self.tableWidgetSupplier.currentRow()
    #     if index < 0:
    #         QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một nhà cung cấp để cập nhật!")
    #         return
    #
    #     # Lấy dữ liệu từ QLineEdit
    #     id = self.lineEditSupplierID.text()
    #     ten = self.lineEditSupplierName.text()
    #     ngaynhaphang = self.lineEditSupplydate.text()
    #     tensanpham = self.lineEditProductname.text()
    #     soluong = self.lineEditQuantity.text()
    #
    #     # Cập nhật vào QTableWidget
    #     self.tableWidgetSupplier.setItem(index, 0, QTableWidgetItem(id))
    #     self.tableWidgetSupplier.setItem(index, 1, QTableWidgetItem(ten))
    #     self.tableWidgetSupplier.setItem(index, 2, QTableWidgetItem(ngaynhaphang))
    #     self.tableWidgetSupplier.setItem(index, 3, QTableWidgetItem(tensanpham))
    #     self.tableWidgetSupplier.setItem(index, 4, QTableWidgetItem(soluong))
    #
    #     QMessageBox.information(self.MainWindow, "Thông báo", "Cập nhật thành công!")
    #
    #     # Cập nhật vào QTableWidget
    #     self.tableWidgetSupplier.setItem(index, 0, QTableWidgetItem(id))
    #     self.tableWidgetSupplier.setItem(index, 1, QTableWidgetItem(ten))
    #     self.tableWidgetSupplier.setItem(index, 2, QTableWidgetItem(ngaynhaphang))
    #     self.tableWidgetSupplier.setItem(index, 3, QTableWidgetItem(tensanpham))
    #     self.tableWidgetSupplier.setItem(index, 4, QTableWidgetItem(soluong))
    #
    #     QMessageBox.information(self.MainWindow, "Thông báo", "Cập nhật thành công!")
    def xuly_cap_nhat(self):
        if self.is_updating:
            return
        self.is_updating = True
        empid = self.lineEditSupplierID.text().strip()
        empname = self.lineEditSupplierName.text().strip()
        password = self.lineEditSupplydate.text().strip()
        role = self.lineEditProductname.text().strip()
        email = self.lineEditQuantity.text().strip()
        if not empid or not empname or not role or not email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            self.is_updating = False
            return

        existing_employee = self.dc.get_supplier_by_categories(empid)
        if not existing_employee:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy nhân viên để cập nhật!")
            self.is_updating = False
            return

        password = existing_employee.Password if not password else password
        employee = Supplier(empid, empname,  password, role, email)
        self.dc.save_update_supplier(employee)
        self.suppliers = self.dc.get_all_suppliers()
        self.show_supplier_gui()

        QMessageBox.information(self, "Thành công", "Nhân viên đã được cập nhật!")
        self.is_updating = False

    def clear_product_detail(self):
        self.lineEditSupplierID.clear()
        self.lineEditSupplierName.clear()
        self.lineEditSupplydate.clear()
        self.lineEditProductname.clear()
        self.lineEditQuantity.clear()
        self.lineEditSearch.clear()
        self.textEditDescription.clear()

        self.show_all_suppliers()
        self.toggle_clear_button()

    def toggle_clear_button(self):
        has_text = any([
            self.lineEditSupplierID.text().strip(),
            self.lineEditSupplydate.text().strip(),
            self.lineEditProductname.text().strip(),
            self.lineEditQuantity.text().strip(),
            self.lineEditSupplierName.text().strip(),
        ])

        self.pushButtonClear.setEnabled(has_text)
    def load_all_suppliers(self):
        self.tableWidgetSupplier.setRowCount(0)
        for employee in self.suppliers:
            row = self.tableWidgetSupplier.rowCount()
            self.tableWidgetSupplier.insertRow(row)

            self.tableWidgetSupplier.setItem(row, 0, QTableWidgetItem(employee.id))
            self.tableWidgetSupplier.setItem(row, 1, QTableWidgetItem(employee.ten))
            self.tableWidgetSupplier.setItem(row, 2, QTableWidgetItem(employee.ngaynhaphang))
            self.tableWidgetSupplier.setItem(row, 3, QTableWidgetItem(employee.tensanpham))
            self.tableWidgetSupplier.setItem(row, 4, QTableWidgetItem(employee.soluong))

    def save_supplier(self):
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


        search_id = self.lineEditSearch.text().strip().lower()

        if not search_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập ID để tìm kiếm.")
            return
        print(f"🔍 Giá trị nhập vào: '{search_id}'")
        if not search_id:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập ID để tìm kiếm.")
            return

        print(f"📋 Danh sách nhà cung cấp: {[s.id for s in self.suppliers]}")

        # Tìm nhà cung cấp, kiểm tra ID có bị None không
        supplier = next((e for e in self.suppliers if e.id and e.id.lower() == search_id), None)

        if supplier:
            self.lineEditSupplierID.setText(supplier.id)
            self.lineEditSupplierName.setText(supplier.ten)
            self.lineEditSupplydate.setText(str(supplier.ngaynhaphang))
            self.lineEditProductname.setText(supplier.tensanpham)
            self.lineEditQuantity.setText(str(supplier.soluong))
        else:
            QMessageBox.warning(self, "Không tìm thấy", f"Không tìm thấy nhà cung cấp có ID: {search_id}")

    # def search_supplier(self):
    #     search_id = self.lineEditSearch.text().strip()
    #     if not search_id:
    #         QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập Supplier ID để tìm kiếm.")
    #         return
    #
    #     supplier = next((s for s in self.suppliers if s.id == search_id), None)
    #
    #     if supplier:
    #         self.lineEditSupplierID.setText(supplier.id)
    #         self.lineEditSupplierName.setText(supplier.ten)
    #         self.lineEditSupplydate.setText(str(supplier.ngaynhaphang))
    #         self.lineEditProductname.setText(supplier.tensanpham)
    #         self.lineEditQuantity.setText(str(supplier.soluong))
    #
    #         description = (
    #             f"Thời gian hợp tác: {supplier.thoigian_hoptac}\n"
    #
    #             f"Chứng nhận chất lượng: {supplier.chung_nhan}\n"
    #
    #             f"Nguồn gốc sản phẩm: {supplier.nguon_goc}\n"
    #
    #             f"Thông tin liên lạc: {supplier.thongtin_lienlac}"
    #         )
    #         self.textEditDescription.setText(description)
    #
    #     for row in range(self.tableWidgetSupplier.rowCount()):
    #         if self.tableWidgetSupplier.item(row, 0).text() == search_id:
    #             for col in range(self.tableWidgetSupplier.columnCount()):
    #                 self.tableWidgetSupplier.item(row, col).setBackground(QColor(255, 255, 0))
    #             break
    #
    #     else:
    #         QMessageBox.warning(self.MainWindow, "Không tìm thấy", f"Không tìm thấy nhà cung cấp có ID: {search_id}")

    def open_help(self):
        file_help = "HElP SUPPLIER.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../help/{file_help}"
        webbrowser.open_new(file_help)



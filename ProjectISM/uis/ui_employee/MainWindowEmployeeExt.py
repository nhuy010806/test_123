import os
import webbrowser

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow

from libs.DataConnector import DataConnector
from libs.ExportTool import ExportTool
from models.Employee import Employee
from uis.ui_employee.MainWindowEmployee import Ui_MainWindow


class MainWindowEmployeeExt(QMainWindow, Ui_MainWindow):
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        self.dc = DataConnector()
        self.employees = self.dc.get_all_employees()
        self.setupUi(self)
        self.setupSignalAndSlot()


        if hasattr(self, 'pushButtonBack'):
            self.pushButtonBack.clicked.connect(self.go_back)

    def go_back(self):
        self.menu_window.show()
        self.close()

    def loadEmployees(self):
        employees_data = self.dc.get_all_employees()
        self.employees = employees_data if employees_data else []  # Đảm bảo danh sách không rỗng
        self.show_employee_gui()

    def showWindow(self):
        self.show()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_employee_gui()
        self.setupSignalAndSlot()
        self.tableWidgetProduct.setRowCount(0)



    def show_employee_gui(self):
        self.tableWidgetProduct.setRowCount(0)
        for product in self.employees:
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            # create 5 columms for each row
            col_proid = QTableWidgetItem(product.EmployeeId)
            col_proname = QTableWidgetItem(product.EmployeeName)
            col_price = QTableWidgetItem(str(product.UserName))
            col_quantity = QTableWidgetItem(str(product.Password))
            col_cateid = QTableWidgetItem(str(product.Role))
            col_email=QTableWidgetItem(product.Email)
            col_level=QTableWidgetItem(product.Level)
            col_shift=QTableWidgetItem(product.Shift)
            col_number=QTableWidgetItem(product.Number)
            col_address=QTableWidgetItem(product.Address)
            # set columm for row
            self.tableWidgetProduct.setItem(row, 0, col_proid)
            self.tableWidgetProduct.setItem(row, 1, col_proname)
            self.tableWidgetProduct.setItem(row, 2, col_price)
            self.tableWidgetProduct.setItem(row, 3, col_quantity)
            self.tableWidgetProduct.setItem(row, 4, col_cateid)
            self.tableWidgetProduct.setItem(row,5,col_email)
            self.tableWidgetProduct.setItem(row,6,col_level)
            self.tableWidgetProduct.setItem(row,7,col_shift)
            self.tableWidgetProduct.setItem(row,8,col_number)
            self.tableWidgetProduct.setItem(row,9,col_address)
    # def show_detail_product(self):
    #     index=self.tableWidgetProduct.currentRow()
    #     if index<0:
    #         return
    #     product=self.employees[index]
    #     self.lineEditId.setText(product.EmployeeId)
    #     self.lineEditName.setText(product.EmployeeName)
    #     self.lineEditUserName.setText(product.UserName)
    #     self.lineEditUserPassword.setText(str(product.Password))
    #     self.lineEditUserRole.setText(product.Role)
    #     self.lineEditEmail.setText(product.Email)
    #     self.lineEditLevel.setText(product.Level)
    #     self.lineEditShift.setText(product.Shift)
    #     self.lineEditNumber.setText(product.Number)
    #     self.lineEditAddress.setText(product.Address)


    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.xuly_luu_moi)
        self.pushButtonUpdate.clicked.connect(self.xuly_cap_nhat)
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.actionImport.triggered.connect(self.import_to_excel)
        self.actionExxport.triggered.connect(self.export_to_excel)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.show_detail_product)
        self.pushButtonClear.clicked.connect(self.clear_product_detail)
        self.pushButtonSearch.clicked.connect(self.search_employee)
        self.pushButtonShowAll.clicked.connect(self.show_all_employees)
        self.actionHelp.triggered.connect(self.open_help)

        self.lineEditId.textChanged.connect(self.toggle_clear_button)
        self.lineEditName.textChanged.connect(self.toggle_clear_button)
        self.lineEditUserName.textChanged.connect(self.toggle_clear_button)
        self.lineEditUserPassword.textChanged.connect(self.toggle_clear_button)
        self.lineEditUserRole.textChanged.connect(self.toggle_clear_button)
        self.lineEditEmail.textChanged.connect(self.toggle_clear_button)
        self.lineEditLevel.textChanged.connect(self.toggle_clear_button)
        self.lineEditShift.textChanged.connect(self.toggle_clear_button)
        self.lineEditNumber.textChanged.connect(self.toggle_clear_button)
        self.lineEditAddress.textChanged.connect(self.toggle_clear_button)
        self.toggle_clear_button()
        self.pushButtonBack.clicked.connect(self.go_back)

    def xuly_luu_moi(self):
        empid = self.lineEditId.text().strip()
        empname = self.lineEditName.text().strip()
        username = self.lineEditUserName.text().strip()
        password = self.lineEditUserPassword.text().strip()
        role = self.lineEditUserRole.text().strip()
        email = self.lineEditEmail.text().strip()
        level = self.lineEditLevel.text().strip()
        shift = self.lineEditShift.text().strip()
        number = self.lineEditNumber.text().strip()
        address = self.lineEditAddress.text().strip()

        if not empid or not empname or not username or not password or not role or not email:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if self.dc.find_index_employee(empid) != -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Nhân viên đã tồn tại!")
            return
        employee = Employee(empid, empname, username, password, role, email, level, shift, number, address)
        self.dc.save_new_employee(employee)
        self.employees = self.dc.get_all_employees()
        self.show_employee_gui()
        QMessageBox.information(self.MainWindow, "Thành công", "Nhân viên mới đã được thêm!")

    def xuly_cap_nhat(self):
        empid = self.lineEditId.text().strip()
        empname = self.lineEditName.text().strip()
        username = self.lineEditUserName.text().strip()
        password = self.lineEditUserPassword.text().strip()
        role = self.lineEditUserRole.text().strip()
        email = self.lineEditEmail.text().strip()
        level = self.lineEditLevel.text().strip()
        shift = self.lineEditShift.text().strip()
        number = self.lineEditNumber.text().strip()
        address = self.lineEditAddress.text().strip()

        if not empid or not empname or not username or not role or not email:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        existing_employee = self.dc.get_employees_by_categories(empid)
        if not existing_employee:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy nhân viên để cập nhật!")
            return
        password = existing_employee.Password if not password else password
        employee = Employee(empid, empname, username, password, role, email, level, shift, number, address)
        self.dc.save_update_employee(employee)
        self.employees = self.dc.get_all_employees()
        self.show_employee_gui()
        QMessageBox.information(self.MainWindow, "Thành công", "Nhân viên đã được cập nhật!")

    def xuly_xoa(self):
        empid = self.lineEditId.text().strip()
        if not empid:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập ID nhân viên cần xóa!")
            return

        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText(f"Bạn có chắc muốn xóa nhân viên [{empid}] không?")
        msgbox.setWindowTitle("Xác nhận xóa")
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if msgbox.exec() == QMessageBox.StandardButton.No:
            return
        self.dc.delete_employee(empid)
        self.employees = self.dc.get_all_employees()
        self.show_employee_gui()
    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Bạn Muốn Thoát phần mềm này?")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Critical)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgbox.setStandardButtons(buttons)
        if msgbox.exec() == QMessageBox.StandardButton.Yes:
            exit()
    def export_to_excel(self):
        filename='../dataset/employee.xlsx'
        extool=ExportTool()
        extool.export_employee_to_excel(filename,self.employees)
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("Đã export excel thành công")
        msgbox.setWindowTitle("Thông báo")
        msgbox.exec()
    def import_to_excel(self):
        filename_cate = "../dataset/employee.xlsx"
        extool = ExportTool()
        self.employees=extool.import_employee_excel(filename_cate)
        self.show_employee_gui()
    def clear_product_detail(self):
        self.lineEditId.setText("")
        self.lineEditName.setText("")
        self.lineEditUserName.setText(str(""))
        self.lineEditUserPassword.setText(str(""))
        self.lineEditUserRole.setText("")
        self.lineEditEmail.setText("")
        self.lineEditShift.setText("")
        self.lineEditLevel.setText("")
        self.lineEditNumber.setText("")
        self.lineEditAddress.setText("")
        self.lineEditId.setFocus()
        self.load_all_employees()
        self.toggle_clear_button()

    # def search_employee(self):
    #     search_id = self.lineEditId.text().strip()
    #
    #     if not search_id:
    #         QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập ID để tìm kiếm.")
    #         return
    #
    #     # Tìm nhân viên theo ID
    #     employee = next((e for e in self.employees if e.EmployeeId == search_id), None)
    #
    #     if employee:
    #         self.lineEditName.setText(employee.EmployeeName)
    #         self.lineEditUserName.setText(employee.UserName)
    #         self.lineEditUserPassword.setText(employee.Password)
    #         self.lineEditUserRole.setText(employee.Role)
    #         self.lineEditEmail.setText(employee.Email)
    #         self.lineEditShift.setText(employee.Shift)
    #         self.lineEditLevel.setText(employee.Level)
    #         self.lineEditNumber.setText(employee.Number)
    #         self.lineEditAddress.setText(employee.Address)
    #
    #         # Cập nhật các trường có ComboBox (nếu có)
    #         if hasattr(self, 'comboBoxLevel'):
    #             self.comboBoxLevel.setCurrentText(employee.Level)
    #         if hasattr(self, 'comboBoxShift'):
    #             self.comboBoxShift.setCurrentText(employee.Shift)
    #
    #     else:
    #         QMessageBox.warning(self.MainWindow, "Không tìm thấy", f"Không tìm thấy nhân viên có ID: {search_id}")

    def show_all_employees(self):
        self.employees = self.dc.get_all_employees()
        self.show_employee_gui()

    def show_detail_product(self):
        index = self.tableWidgetProduct.currentRow()
        if index < 0:
            return
        product = self.employees[index]
        self.lineEditId.setText(product.EmployeeId)
        self.lineEditName.setText(product.EmployeeName)
        self.lineEditUserName.setText(product.UserName)
        self.lineEditUserPassword.setText(str(product.Password))
        self.lineEditUserRole.setText(product.Role)
        self.lineEditEmail.setText(product.Email)
        self.lineEditLevel.setText(product.Level)
        self.lineEditShift.setText(product.Shift)
        self.lineEditNumber.setText(product.Number)
        self.lineEditAddress.setText(product.Address)
        for i in range(self.tableWidgetProduct.rowCount()):
            for j in range(self.tableWidgetProduct.columnCount()):
                if self.tableWidgetProduct.item(i, j):
                    self.tableWidgetProduct.item(i, j).setBackground(QColor(Qt.GlobalColor.white))
        pastel_color = QColor("#FFFACD")
        for j in range(self.tableWidgetProduct.columnCount()):
            if self.tableWidgetProduct.item(index, j):
                self.tableWidgetProduct.item(index, j).setBackground(pastel_color)

    def show_search_result_in_table(self, employee):

        self.tableWidgetProduct.setRowCount(0)
        row = self.tableWidgetProduct.rowCount()
        self.tableWidgetProduct.insertRow(row)
        col_proid = QTableWidgetItem(employee.EmployeeId)
        col_proname = QTableWidgetItem(employee.EmployeeName)
        col_price = QTableWidgetItem(str(employee.UserName))
        col_quantity = QTableWidgetItem(str(employee.Password))
        col_cateid = QTableWidgetItem(str(employee.Role))
        col_email = QTableWidgetItem(employee.Email)
        col_level = QTableWidgetItem(employee.Level)
        col_shift = QTableWidgetItem(employee.Shift)
        col_number = QTableWidgetItem(employee.Number)
        col_address = QTableWidgetItem(employee.Address)


        self.tableWidgetProduct.setItem(row, 0, col_proid)
        self.tableWidgetProduct.setItem(row, 1, col_proname)
        self.tableWidgetProduct.setItem(row, 2, col_price)
        self.tableWidgetProduct.setItem(row, 3, col_quantity)
        self.tableWidgetProduct.setItem(row, 4, col_cateid)
        self.tableWidgetProduct.setItem(row, 5, col_email)
        self.tableWidgetProduct.setItem(row, 6, col_level)
        self.tableWidgetProduct.setItem(row, 7, col_shift)
        self.tableWidgetProduct.setItem(row, 8, col_number)
        self.tableWidgetProduct.setItem(row, 9, col_address)


        pastel_color = QColor("#B2D8D8")
        for j in range(self.tableWidgetProduct.columnCount()):
            if self.tableWidgetProduct.item(row, j):
                self.tableWidgetProduct.item(row, j).setBackground(pastel_color)

    def search_employee(self):
        search_id = self.lineEditId.text().strip()

        if not search_id:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập ID để tìm kiếm.")
            return


        employee = next((e for e in self.employees if e.EmployeeId == search_id), None)

        if employee:

            self.lineEditName.setText(employee.EmployeeName)
            self.lineEditUserName.setText(employee.UserName)
            self.lineEditUserPassword.setText(employee.Password)
            self.lineEditUserRole.setText(employee.Role)
            self.lineEditEmail.setText(employee.Email)
            self.lineEditShift.setText(employee.Shift)
            self.lineEditLevel.setText(employee.Level)
            self.lineEditNumber.setText(employee.Number)
            self.lineEditAddress.setText(employee.Address)
            self.show_search_result_in_table(employee)
            if hasattr(self, 'comboBoxLevel'):
                self.comboBoxLevel.setCurrentText(employee.Level)
            if hasattr(self, 'comboBoxShift'):
                self.comboBoxShift.setCurrentText(employee.Shift)

        else:
            QMessageBox.warning(self.MainWindow, "Không tìm thấy", f"Không tìm thấy nhân viên có ID: {search_id}")

    def load_all_employees(self):
        self.tableWidgetProduct.setRowCount(0)
        for employee in self.employees:
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)

            self.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(employee.EmployeeId))
            self.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(employee.EmployeeName))
            self.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(employee.UserName))
            self.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(employee.Password))
            self.tableWidgetProduct.setItem(row, 4, QTableWidgetItem(employee.Role))
            self.tableWidgetProduct.setItem(row, 5, QTableWidgetItem(employee.Email))
            self.tableWidgetProduct.setItem(row, 6, QTableWidgetItem(employee.Level))
            self.tableWidgetProduct.setItem(row, 7, QTableWidgetItem(employee.Shift))
            self.tableWidgetProduct.setItem(row, 8, QTableWidgetItem(employee.Number))
            self.tableWidgetProduct.setItem(row, 9, QTableWidgetItem(employee.Address))

    def open_help(self):
        file_help = "HDSD.pdf"
        current_path = os.getcwd()
        file_help = f"{current_path}/../help/{file_help}"
        webbrowser.open_new(file_help)

    def toggle_clear_button(self):
        has_text = any([
            self.lineEditId.text().strip(),
            self.lineEditName.text().strip(),
            self.lineEditUserName.text().strip(),
            self.lineEditUserPassword.text().strip(),
            self.lineEditUserRole.text().strip(),
            self.lineEditEmail.text().strip(),
            self.lineEditLevel.text().strip(),
            self.lineEditShift.text().strip(),
            self.lineEditNumber.text().strip(),
            self.lineEditAddress.text().strip()
        ])

        self.pushButtonClear.setEnabled(has_text)

    # def show_all_products(self):
    #     self.products = self.dc.get_all_products()
    #
    #     # Hiển thị lên giao diện
    #     self.show_products_gui()


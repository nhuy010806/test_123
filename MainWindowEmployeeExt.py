from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from models.DataConnector import DataConnector
from models.ExportTool import ExportTool
from models.User import Employee
from ui.MainWindowEmployee import Ui_MainWindow

class MainWindowEmployeeExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.employees = self.dc.get_all_employees()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.show_employee_gui()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def show_employee_gui(self):
        """Hiển thị danh sách nhân viên trong bảng (Không bao gồm Password)."""
        self.tableWidgetProduct.setRowCount(0)
        for employee in self.employees:
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)

            col_empid = QTableWidgetItem(employee.EmployeeId)
            col_empname = QTableWidgetItem(employee.EmployeeName)
            col_username = QTableWidgetItem(employee.UserName)

            self.tableWidgetProduct.setItem(row, 0, col_empid)
            self.tableWidgetProduct.setItem(row, 1, col_empname)
            self.tableWidgetProduct.setItem(row, 2, col_username)

    def setupSignalAndSlot(self):
        """Gán sự kiện cho các nút."""
        self.pushButtonSave.clicked.connect(self.xuly_luu)
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonexit_2.clicked.connect(self.exit_program)
        self.pushButtonexport_2.clicked.connect(self.export_to_excel)
        self.pushButtonImport_2.clicked.connect(self.import_to_excel)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.show_detail_employee)

    def xuly_luu(self):
        """Xử lý lưu nhân viên mới hoặc cập nhật thông tin nhân viên."""
        empid = self.lineEditId.text().strip()
        empname = self.lineEditName.text().strip()
        username = self.lineEditUserName.text().strip()
        password=self.lineEditUserPassword.text().strip()

        if not empid or not empname or not username:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Không lấy password từ UI
        existing_employee = self.dc.get_employees_by_categories(empid)
        password = existing_employee.Password if existing_employee else ""

        employee = Employee(empid, empname, username, password)
        index = self.dc.find_index_employee(empid)

        if index == -1:
            self.dc.save_new_employee(employee)
        else:
            self.dc.save_update_employee(employee)

        self.employees = self.dc.get_all_employees()
        self.show_employee_gui()

    def xuly_xoa(self):
        """Xử lý xóa nhân viên."""
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

    def show_detail_employee(self):
        """Hiển thị chi tiết nhân viên khi chọn trong bảng."""
        index = self.tableWidgetProduct.currentRow()
        if index < 0 or index >= len(self.employees):
            return

        employee = self.employees[index]
        self.lineEditId.setText(employee.EmployeeId)
        self.lineEditName.setText(employee.EmployeeName)
        self.lineEditUserName.setText(employee.UserName)
        self.lineEditUserPassword.setText(employee.Password)
    def exit_program(self):
        msgbox = QMessageBox(self.MainWindow)
        msgbox.setText("e mun thoat phan mem nay ha")
        msgbox.setWindowTitle("xac nhan thoat")
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

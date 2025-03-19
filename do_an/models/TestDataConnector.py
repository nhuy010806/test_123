from models.DataConnector import DataConnector

dc = DataConnector()
employees = dc.get_all_employees()

print("Danh sách nhân viên từ JSON:")
for emp in employees:
    print(emp.EmployeeId, emp.EmployeeName, emp.UserName,emp.Password,emp.Role,emp.Email,
          emp.Level,emp.Shift,emp.Number,emp.Address)


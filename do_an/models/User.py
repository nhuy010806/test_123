class Employee:
    def __init__(self, EmployeeId,EmployeeName,UserName,Password,Role,Email,Level,Shift,Number,Address):
        self.EmployeeId=EmployeeId
        self.EmployeeName=EmployeeName
        self.UserName=UserName
        self.Password=Password
        self.Role=Role
        self.Email=Email
        self.Level=Level
        self.Shift=Shift
        self.Number=Number
        self.Address=Address
    def __str__(self):
        return (f"{self.EmployeeId}\t{self.EmployeeName}\t{self.UserName}\t{self.Role}\t{self.Email}\t{self.Level}\t"
                f"{self.Shift}\t{self.Number}\t{self.Address}")
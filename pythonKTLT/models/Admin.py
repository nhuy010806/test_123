class Admin:
    def __init__(self, adminId, adminName, adminUsername, adminPass):
        self.adminId = adminId
        self.adminName = adminName
        self.adminUsername = adminUsername
        self.adminPass = adminPass

    def __str__(self):
        return f"{self.adminId}\t{self.adminName}"
class Staff:
    def __init__(self, staffId, staffName, staffAddress,staffUsername, staffPassword):
        self.staffId = staffId
        self.staffName = staffName
        self.staffAddress = staffAddress
        self.staffUsername=staffUsername
        self.staffPassword = staffPassword

    def __str__(self):
            return f"{self.staffId}\t{self.staffName}\t{self.staffAddress}"


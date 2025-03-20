class User:
    def __init__(self, userid,name,username,password):
        self.userid = userid
        self.name=name
        self.username=username
        self.password=password
    def __str__(self):
        return f"{self.userid}\t{self.name}\t{self.username}\t{self.password}"


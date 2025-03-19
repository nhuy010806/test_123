class Employee:
    def __init__(self, id,name,username,password):
        self.id = id
        self.name=name
        self.username=username
        self.password=password
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.username}\t{self.password}"


class Category:
    def __init__(self, cateid,description=""):
        self.cateid = cateid
        self.description = description

    def __str__(self):
        return f"{self.cateid}\t{self.description}"
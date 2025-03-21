class Book:
    def __init__(self, bookid, bookname,author,year,quantity):
        self.bookid = bookid
        self.bookname=bookname
        self.author=author
        self.year=year
        self.quantity=quantity

    def __str__(self):
        return f"{self.bookid}\t{self.bookname}\t{self.author}\t{self.year}\t{self.quantity}"

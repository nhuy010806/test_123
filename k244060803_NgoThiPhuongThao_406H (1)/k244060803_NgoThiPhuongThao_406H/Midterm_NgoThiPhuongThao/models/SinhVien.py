from Midterm_NgoThiPhuongThao.models.User import User


class SinhVien(User):
    def __init__(self, userid, name, username, password, classid,borrowed_books):
        super().__init__(userid, name, username, password)
        self.classid = classid
        self.borrowed_books = borrowed_books

    def __str__(self):
        return super().__str__() + f"{self.classid}\t{self.borrowed_books}"
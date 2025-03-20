from Midterm_NgoThiPhuongThao.models.User import User


class GiangVien(User):
    def __init__(self, userid, name, username, password, khoa):
        super().__init__(userid, name, username, password)
        self.khoa = khoa

    def __str__(self):
        return super().__str__() + f"{self.khoa}"

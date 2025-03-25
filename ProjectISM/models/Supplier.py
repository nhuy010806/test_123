class Supplier:
    def __init__(self, id, ten, ngaynhaphang, tensanpham, loaihopdong, thoigian_hoptac="", chung_nhan="", nguon_goc="",thongtin_lienlac=""):
        self.id = id
        self.ten = ten
        self.ngaynhaphang = ngaynhaphang
        self.tensanpham = tensanpham
        self.loaihopdong = loaihopdong
        self.thoigian_hoptac = thoigian_hoptac
        self.chung_nhan = chung_nhan
        self.nguon_goc = nguon_goc
        self.thongtin_lienlac=thongtin_lienlac

    def __str__(self):
        return (f"{self.id}\t{self.ten}\t{self.ngaynhaphang}\t{self.tensanpham}\t{self.loaihopdong}\t{self.thoigian_hoptac}\t{self.chung_nhan}\t{self.nguon_goc}\t{self.thongtin_lienlac}")

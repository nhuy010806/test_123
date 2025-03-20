class PhieuMuonSach:
    def __init__(self, muonid, nguoimuon, sach):
        self.muonid = muonid
        self.nguoimuon = nguoimuon
        self.sach = sach

    def __str__(self):
        return f" {self.muonid}\t {self.nguoimuon}\t {self.sach}"
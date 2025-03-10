class Supplier:
    def __init__(self,id, name, password, contact_name, email, phone, address):
        self.id = id
        self.name = name  # Tên công ty cung cấp
        self.contact_name = contact_name  # Tên người liên hệ
        self.email = email
        self.phone = phone
        self.password=password
        self.address = address  # Địa chỉ của nhà cung cấp
    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.password}\t{self.contact_name}\t{self. email}\t{self.phone}\t{self. address}"
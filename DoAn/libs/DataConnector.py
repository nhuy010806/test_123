from DoAn.libs.JsonFileFactory import JsonFileFactory
from DoAn.models.Supplier import Supplier

class DataConnector:
    def __init__(self):
        self.suppliers = []

    def load_suppliers(self, filename):
        jff = JsonFileFactory()
        self.suppliers = jff.read_data([], filename)

    def get_all_suppliers(self):
        suppliers = []
        jff = JsonFileFactory()
        filename = "../dataset/suppliers.json"
        suppliers = jff.read_data(filename, Supplier)
        return suppliers
    def find_index_supplier(self,supplier_id):
        self.suppliers = self.get_all_suppliers()
        for i in range(len(self.suppliers)):
            supplier=self.suppliers[i]
            if supplier.id==supplier_id:
                return i
        return -1
    def save_new_supplier(self,supplier):
        suppliers = self.get_all_suppliers()
        suppliers.append(supplier)
        jff = JsonFileFactory()
        filename = "../dataset/suppliers.json"
        jff.write_data(suppliers, filename)
    def save_update_supplier(self,current_supplier):
        index=self.find_index_supplier(current_supplier.id)
        if index!=-1:
            self.suppliers[index]=current_supplier
            jff = JsonFileFactory()
            filename = "../dataset/suppliers.json"
            jff.write_data(self.suppliers,filename)

    def delete_supplier(self,supplier_id):

        index = self.find_index_supplier(supplier_id)
        if index != -1:
            self.suppliers.pop(index)
            jff = JsonFileFactory()
            filename = "../dataset/suppliers.json"
            jff.write_data(self.suppliers, filename)

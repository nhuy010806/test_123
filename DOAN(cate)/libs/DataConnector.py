from DOAN.libs.JsonFileFactory import JsonFileFactory
from DOAN.models.Category import Category

class DataConnector:
    def get_all_categories(self):
        jff = JsonFileFactory()
        filename = "../dataset/categories.json"
        return jff.read_data(filename, Category)

    def save_newcategory(self, category):
        categories = self.get_all_categories()
        categories.append(category)
        jff = JsonFileFactory()
        filename = "../dataset/categories.json"
        jff.write_data(categories, filename)

    def find_index_category(self, cateid):
        categories = self.get_all_categories()
        for i, category in enumerate(categories):
            if category.cateid == cateid:
                return i
        return -1

    def save_update_category(self, current_category):
        index = self.find_index_category(current_category.cateid)
        if index != -1:
            categories = self.get_all_categories()
            categories[index] = current_category
            jff = JsonFileFactory()
            filename = "../dataset/categories.json"
            jff.write_data(categories, filename)

    def delete_category(self, cateid):
        """ Xóa Cate ID khỏi danh sách """
        categories = self.get_all_categories()
        index = self.find_index_category(cateid)
        if index != -1:
            categories.pop(index)
            jff = JsonFileFactory()
            filename = "../dataset/categories.json"
            jff.write_data(categories, filename)
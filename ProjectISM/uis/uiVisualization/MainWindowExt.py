import pandas as pd
from PyQt6.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from uis.uiVisualization.MainWindow import Ui_MainWindow


class MainWindowEx(QMainWindow,Ui_MainWindow):
    def __init__(self, menu_window):
        super().__init__()
        self.menu_window = menu_window
        # self.parent = parent
        self.setupUi(self)
        self.setupPlot()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
       # self.setupPlot()
        self.pushButtonBarChart.clicked.connect(self.showBarChart)
        self.pushButtonLineChart.clicked.connect(self.showLinePlotChart)
        self.pushButtonPieChart.clicked.connect(self.showPieChart)
        self.pushButtonShowAll_2.clicked.connect(self.showAllObject)
        self.pushButtonPieShift.clicked.connect(self.showPieShift)
        self.pushButtonDistribution.clicked.connect(self.showDistribution)
        self.pushButtonExit.clicked.connect(self.xuly_back)

    def show(self):
        QMainWindow.show(self)
    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.verticalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canvas)
    def load_data(self, file_path, sheet_name=None):
        """Hàm đọc dữ liệu từ file Excel và xử lý lỗi."""
        try:
            if sheet_name:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
            else:
                df = pd.read_excel(file_path)
            return df
        except Exception as e:
            print(f"Lỗi khi đọc file Excel: {e}")
            return None
    def showBarChart(self):
        file_path = '../dataset/products.xlsx'
        sheet_name = 'Products'
        # Load data
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Xóa figure cũ
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # Gộp số lượng sản phẩm theo danh mục và tên sản phẩm
        df_grouped = df.groupby(["Category Name", "Product Name"], as_index=False)["Quantity"].sum()
        # Danh sách danh mục sản phẩm
        unique_categories = df_grouped["Category Name"].unique()
        # Tạo màu sắc riêng cho từng danh mục
        colors = plt.cm.Set2(range(len(unique_categories)))
        category_colors = {category: colors[i] for i, category in enumerate(unique_categories)}
        # Gán màu sắc theo danh mục
        df_grouped["color"] = df_grouped["Category Name"].map(category_colors)
        # Vẽ biểu đồ cột
        ax.bar(df_grouped["Product Name"], df_grouped["Quantity"], color=df_grouped["color"])
        # Thiết lập tiêu đề và nhãn
        ax.set_title("Số lượng sản phẩm theo danh mục")
        ax.set_xticks(range(len(df_grouped["Product Name"])))
        ax.set_xticklabels(df_grouped["Product Name"], rotation=45, ha="right", fontsize=7)  # Giảm fontsize nếu cần
        ax.set_ylabel("Số lượng")
        # Cập nhật lại canvas
        self.canvas.draw()
        print(df.columns)


    def showLinePlotChart(self):
        file_path = '../dataset/products.xlsx'
        df = self.load_data(file_path)
        # Chuyển cột Date sang dạng datetime
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', dayfirst=True)
        # Gộp Quantity theo ngày
        df_grouped = df.groupby('Date', as_index=False)['Quantity'].sum()
        # Sắp xếp theo ngày
        df_grouped = df_grouped.sort_values(by='Date')
        # Xóa figure cũ
        self.figure.clear()
        # Tạo subplot mới
        ax = self.figure.add_subplot(111)
        # Vẽ line plot
        sns.lineplot(data=df_grouped, x='Date', y='Quantity', marker='o', color='orange', ax=ax)
        # Cài đặt nhãn và tiêu đề
        ax.set_xlabel("Ngày")
        ax.set_ylabel("Số lượng")
        ax.set_title("Số lượng theo thời gian")
        # Xoay nhãn ngày để dễ đọc
        ax.tick_params(axis='x', rotation=45, labelsize=7)
        # Hiển thị lưới
        ax.grid()
        # Cập nhật lại canvas
        self.canvas.draw()
    def showPieChart(self):
        file_path = '../dataset/products.xlsx'
        df = self.load_data(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        category_data = df.groupby("Category Name")["Quantity"].sum()
        ax.pie(category_data, labels=category_data.index, autopct='%1.2f%%', startangle=140)
        ax.set_title("Phân bổ danh mục theo số lượng")
        self.canvas.draw()
    ##################################################
    def showAllObject(self):
        file_path = '../dataset/employee.xlsx'
        df = self.load_data(file_path)
        num_employees = len(df.index -1)
        self.labelEmployee.setText(f"{num_employees}")
        #######
        file_path1 = '../dataset/products.xlsx'
        df1 = self.load_data(file_path1)
        num_prodcuts = len(df1.index -1)
        self.labelProduct.setText(f"{num_prodcuts}")
        #######
        file_path2 = '../dataset/suppliers.xlsx'
        df2 = self.load_data(file_path2)
        num_suppliers = len(df2.index -1)
        self.labelSupplier.setText(f"{num_suppliers}")
        #######
        file_path4 = '../dataset/categories.json'  # Đường dẫn file JSON
        df4 = pd.read_json(file_path4)  # Đọc file JSON
        num_cate = len(df4.index -1)   # Số lượng nhà cung cấp
        self.labelCategory.setText(f"{num_cate}")  # Hiển thị trên label
    def showPieShift(self):
        file_path = '../dataset/employee.xlsx'
        df = pd.read_excel(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # Đếm số nhân viên theo ca làm việc
        shift_counts = df['Shift'].value_counts()
        # Vẽ biểu đồ tròn trên ax
        ax.pie(shift_counts, labels=shift_counts.index, autopct='%1.2f%%', startangle=140,
               colors=plt.cm.Paired.colors)  # Sử dụng màu tự động
        ax.set_title("Phân bổ nhân viên theo ca làm việc")
        self.canvas.draw()
    def showDistribution(self):
        file_path = '../dataset/suppliers.xlsx'
        df = pd.read_excel(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # Kiểm tra tên cột
        print(df.columns)
        # Đảm bảo cột đúng tên và không có NaN
        column_name = 'Số Lượng'  # Thay bằng tên chính xác
        if column_name in df.columns:
            sns.histplot(df[column_name].dropna(), kde=True, color='r', bins=20, ax=ax)
            ax.set_xlabel('Số lượng sản phẩm')
            ax.set_ylabel('Tần suất')
            ax.set_title('Phân phối số lượng sản phẩm theo nhà cung cấp')
            ax.grid(True)
            self.canvas.draw()
        else:
            print(f"Cột '{column_name}' không tồn tại trong file Excel.")
    def xuly_back(self):
        self.menu_window.show()
        self.close()















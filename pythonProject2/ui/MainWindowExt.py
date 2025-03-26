
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from ui.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupPlot()
        self.pushButtonBarChart.clicked.connect(self.showBarChart)
        self.pushButtonLineChart.clicked.connect(self.showLinePlotChart)
        self.pushButtonPieChart.clicked.connect(self.showPieChart)
        # self.pushButtonExit.clicked.connect(self.processExit)

    def show(self):
        self.MainWindow.show()

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
        file_path = '../dataset_visual/products.xlsx'
        sheet_name = 'Products'

        # Load data
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Xóa figure cũ
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        # Gộp số lượng sản phẩm theo danh mục và tên sản phẩm
        df_grouped = df.groupby(["Cate ID", "Product Name"], as_index=False)["Quantity"].sum()

        # Danh sách danh mục sản phẩm
        unique_categories = df_grouped["Cate ID"].unique()

        # Tạo màu sắc riêng cho từng danh mục
        colors = plt.cm.Set2(range(len(unique_categories)))
        category_colors = {category: colors[i] for i, category in enumerate(unique_categories)}

        # Gán màu sắc theo danh mục
        df_grouped["color"] = df_grouped["Cate ID"].map(category_colors)

        # Vẽ biểu đồ cột
        ax.bar(df_grouped["Product Name"], df_grouped["Quantity"], color=df_grouped["color"])

        # Thiết lập tiêu đề và nhãn
        ax.set_title("Số lượng sản phẩm theo danh mục")
        ax.set_xticks(range(len(df_grouped["Product Name"])))
        ax.set_xticklabels(df_grouped["Product Name"], rotation=45, ha="right", fontsize=7)  # Giảm fontsize nếu cần
        ax.set_ylabel("Số lượng")

        # Cập nhật lại canvas
        self.canvas.draw()

    def showLinePlotChart(self):
        file_path = '../dataset_visual/products.xlsx'
        df = self.load_data(file_path)
        # Chuyển cột Date sang dạng datetime
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', dayfirst=True)
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
        file_path = '../dataset_visual/products.xlsx'
        df = self.load_data(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        category_data = df.groupby("Cate ID")["Quantity"].sum()
        ax.pie(category_data, labels=category_data.index, autopct='%1.2f%%', startangle=140)
        ax.set_title("Phân bổ danh mục theo số lượng")
        self.canvas.draw()
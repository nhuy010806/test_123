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

        self.setupUi(self)
        self.setupPlot()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

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

        df = pd.read_excel(file_path, sheet_name=sheet_name)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        df_grouped = df.groupby(["Category Name", "Product Name"], as_index=False)["Quantity"].sum()
        unique_categories = df_grouped["Category Name"].unique()
        colors = plt.cm.Set2(range(len(unique_categories)))
        category_colors = {category: colors[i] for i, category in enumerate(unique_categories)}
        df_grouped["color"] = df_grouped["Category Name"].map(category_colors)

        ax.bar(df_grouped["Product Name"], df_grouped["Quantity"], color=df_grouped["color"])
        ax.set_title("Số lượng sản phẩm theo danh mục")
        ax.set_xticks(range(len(df_grouped["Product Name"])))
        ax.set_xticklabels(df_grouped["Product Name"], rotation=45, ha="right", fontsize=7)  # Giảm fontsize nếu cần
        ax.set_ylabel("Số lượng")

        self.canvas.draw()
        print(df.columns)

    def showLinePlotChart(self):
        file_path = '../dataset/products.xlsx'
        df = self.load_data(file_path)

        if df is not None and 'Date' in df.columns and 'Quantity' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', dayfirst=True, errors='coerce')
            df = df.dropna(subset=['Date'])

            df_grouped = df.groupby('Date', as_index=False)['Quantity'].sum()
            df_grouped = df_grouped.sort_values(by='Date')
            self.figure.clear()

            ax = self.figure.add_subplot(111)
            sns.lineplot(data=df_grouped, x='Date', y='Quantity', marker='o', color='orange', ax=ax)

            ax.set_xlabel("Ngày")
            ax.set_ylabel("Số lượng")
            ax.set_title("Số lượng theo thời gian")

            ax.tick_params(axis='x', rotation=45, labelsize=7)

            ax.grid()

            self.canvas.draw()
        else:
            print("Dữ liệu không hợp lệ hoặc thiếu cột 'Date' và 'Quantity'")

    def showPieChart(self):
        file_path = '../dataset/products.xlsx'
        df = self.load_data(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        category_data = df.groupby("Category Name")["Quantity"].sum()
        ax.pie(category_data, labels=category_data.index, autopct='%1.2f%%', startangle=140)
        ax.set_title("Phân bổ danh mục theo số lượng")
        self.canvas.draw()

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

        file_path4 = '../dataset/categories.json'
        df4 = pd.read_json(file_path4)
        num_cate = len(df4.index -1)
        self.labelCategory.setText(f"{num_cate}")
    def showPieShift(self):
        file_path = '../dataset/employee.xlsx'
        df = pd.read_excel(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        shift_counts = df['Shift'].value_counts()
        ax.pie(shift_counts, labels=shift_counts.index, autopct='%1.2f%%', startangle=140,
               colors=plt.cm.Paired.colors)  # Sử dụng màu tự động
        ax.set_title("Phân bổ nhân viên theo ca làm việc")
        self.canvas.draw()
    def showDistribution(self):
        file_path = '../dataset/suppliers.xlsx'
        df = pd.read_excel(file_path)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        print(df.columns)

        column_name = 'Số Lượng'
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















import os
import webbrowser
import subprocess
import sys

def open_pdf():
    """Mở file HDSD.pdf trong thư mục help"""
    file_help = "HDSD.pdf"

    # Lấy đường dẫn thư mục chứa file hiện tại
    current_path = os.path.dirname(os.path.abspath(__file__))

    # Đường dẫn đầy đủ đến file PDF trong thư mục help
    file_help_path = os.path.join(current_path, "help", file_help)

    # In ra để kiểm tra đường dẫn
    print(f"📂 Đang tìm file tại: {file_help_path}")

    # Kiểm tra xem file có tồn tại không
    if not os.path.exists(file_help_path):
        print(f"⚠️ Không tìm thấy tệp: {file_help_path}")
        return

    # Thử mở file bằng phương pháp hệ điều hành
    try:
        if sys.platform == "win32":  # Windows
            os.startfile(file_help_path)
        elif sys.platform == "darwin":  # macOS
            subprocess.call(["open", file_help_path])
        else:  # Linux
            subprocess.call(["xdg-open", file_help_path])
        print("✅ Đã mở file PDF thành công!")
    except Exception as e:
        print(f"❌ Lỗi khi mở file PDF: {e}")

# Gọi hàm để kiểm tra
open_pdf()

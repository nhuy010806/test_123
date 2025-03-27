from PyQt6.QtWidgets import QPushButton

class AlwaysDisabledButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setEnabled(False)  # Luôn vô hiệu hóa
        self.setStyleSheet("""
            QPushButton {
                background-color: #D3D3D3;  /* Màu xám */
                color: #A0A0A0; /* Màu chữ xám */
                border: 1px solid #A9A9A9;  /* Viền xám */
            }
        """)

    def setEnabled(self, enabled: bool):
        super().setEnabled(False)  # Chặn bật lại

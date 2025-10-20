from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swiss Tournament App")
        self.resize(900, 600)

        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.addWidget(QLabel("Hello, Swiss!", alignment=Qt.AlignCenter))
        self.setCentralWidget(central)

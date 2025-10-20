import sys
from PySide6.QtWidgets import QApplication
from app.ui.app_window import AppWindow

def main() -> int:
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())

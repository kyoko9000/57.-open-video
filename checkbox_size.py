# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("""
            QCheckBox::indicator{
                width: 40px;
                height: 40px;
            }
        """)
        self.uic.verticalLayout_2.addWidget(self.checkbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
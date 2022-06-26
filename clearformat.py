# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.textedit = QTextEdit()
        self.uic.verticalLayout_2.addWidget(self.textedit)

        self.uic.pushButton.clicked.connect(self.format_font)

    def format_font(self):
        a = self.textedit.toPlainText()
        self.textedit.setText(a)
        self.textedit.selectAll()
        self.textedit.setAlignment(QtCore.Qt.AlignHCenter)
        font = QFont()
        font.setPointSize(20)
        self.textedit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
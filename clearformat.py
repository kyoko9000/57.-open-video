# ************************** man hinh loai 2 *************************
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.textedit = QTextEdit()
        self.uic.verticalLayout_2.addWidget(self.textedit)
        self.uic.pushButton.clicked.connect(self.correct)

    def correct(self):
        self.textedit.selectAll()
        # self.textedit.setCurrentCharFormat(QtGui.QTextCharFormat())

        # cursor = self.textedit.textCursor()
        # # cursor.select(QtGui.QTextCursor.Document)
        # cursor.setCharFormat(QtGui.QTextCharFormat())
        # cursor.clearSelection()
        self.textedit.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
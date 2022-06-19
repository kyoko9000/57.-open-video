# ************************** man hinh loai 2 *************************
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.show_video)

        # QMediaPlayer
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp4')))

        # Set widget
        self.videoWidget = QVideoWidget()
        self.uic.verticalLayout_2.addWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def show_video(self):
        # Play
        self.mediaPlayer.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
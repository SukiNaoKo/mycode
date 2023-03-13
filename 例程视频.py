import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(400, 400)

        self.video_widget = QVideoWidget(self)
        self.video_widget.resize(200, 200)

        self.video_player = QMediaPlayer()
        self.video_player.setMedia(QMediaContent(QUrl.fromLocalFile(r"D:\延时摄影\1  z5.mp4")))
        self.video_player.setVolume(40)
        self.video_player.setVideoOutput(self.video_widget)
        self.video_player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./cat.ico'))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

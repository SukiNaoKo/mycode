import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5 import uic


class Mywindow(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./mycode.ui")
        self.openfileButton = self.ui.pushButton
        self.fnamelist = self.ui.lineEdit
        self.openfileButton.clicked.connect(self.select_dir)

    def select_dir(self):
        self.fname = QFileDialog.getOpenFileName(self,'选择视频文件', '/')
        self.filename, self.filetype = self.fname
        self.fnamelist.setText(self.filename)
        print(self.filename)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    myui = Mywindow()


    myui.ui.show()



    # 程序进行循环等待状态
    app.exec()
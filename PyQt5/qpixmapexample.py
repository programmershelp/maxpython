import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        pixmap = QPixmap('python.png')

        labelImg = QLabel()
        labelImg.setPixmap(pixmap)
        #this makes the label the size of the image
        labelSize = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        labelSize.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(labelImg)
        vbox.addWidget(labelSize)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap Example')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
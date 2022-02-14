import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        color = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('QColorDialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
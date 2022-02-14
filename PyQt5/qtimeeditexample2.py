import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl = QLabel('QTimeEdit Example')

        timeEdit = QTimeEdit(self)
        #set to current time
        timeEdit.setTime(QTime.currentTime())
        #set the time range
        timeEdit.setTimeRange(QTime(6, 00, 00), QTime(22, 00, 00))
        timeEdit.setDisplayFormat('hh:mm:ss')
        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeEdit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

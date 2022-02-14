import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl = QLabel('QDateEdit Example')

        dateedit = QDateEdit(self)
        #set to current date
        dateedit.setDate(QDate.currentDate())
        #set the date range
        dateedit.setDateRange(QDate(2022, 1, 1), QDate(2022, 12, 31))
        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

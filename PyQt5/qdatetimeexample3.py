from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate
import sys
 
def showDate():
    print(dateedit.date().toPyDate())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(300, 300, 300, 200)
win.setWindowTitle("QDateEdit Example")
 
dateedit = QtWidgets.QDateEdit(win)
#set to current date
dateedit.setDate(QDate.currentDate())
#set the minimum date
dateedit.setMinimumDate(QDate(2022, 1, 1))
#set the maximum date
dateedit.setMinimumDate(QDate(1970, 1, 1))
dateedit.setMaximumDate(QDate(2022, 12, 31))
dateedit.move(50,50)
 
button = QtWidgets.QPushButton(win)
button.setText("Press me")
button.clicked.connect(showDate)
button.move(50,100)
 
win.show()
sys.exit(app.exec_())
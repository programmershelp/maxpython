from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTime
import sys
 
def showTime():
    print(timeEdit.time().toPyTime())
 
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(300, 300, 300, 200)
win.setWindowTitle("QTimeEdit Example")
 
timeEdit = QtWidgets.QTimeEdit(win)
#set to current date
timeEdit.setTime(QTime.currentTime())
#set the time range
timeEdit.setTimeRange(QTime(6, 00, 00), QTime(22, 00, 00))
timeEdit.setDisplayFormat('hh:mm:ss')
timeEdit.move(50,50)
 
button = QtWidgets.QPushButton(win)
button.setText("Press me")
button.clicked.connect(showTime)
button.move(50,100)
 
win.show()
sys.exit(app.exec_())
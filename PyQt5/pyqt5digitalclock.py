# importing required libraries
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
 
 
class Window(QWidget):
 
    def __init__(self):
        super().__init__()
        # create the main window
        self.setGeometry(100, 100, 800, 400)
        # creating a vertical layout
        layout = QVBoxLayout()
        # creating font object
        font = QFont('Arial', 120, QFont.Bold)
        # crate the label
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        layout.addWidget(self.label)
        self.setLayout(layout)
        # create a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        # update the timer every second
        timer.start(1000)
 

    def showTime(self):
        # getting current time
        current_time = QTime.currentTime()
        # convert QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.label.setText(label_time)
 
 
# create app
App = QApplication(sys.argv)
window = Window()
window.show()
 
# start the app
App.exit(App.exec_())
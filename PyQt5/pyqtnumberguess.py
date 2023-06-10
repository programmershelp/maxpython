from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Number Guessing Game")
        self.setGeometry(100, 100, 340, 350)
        self.UiComponents()
        self.show()
        self.number = 0
 
    # method for components
    def UiComponents(self):
        head = QLabel("Number Guessing Game", self)
        head.setGeometry(20, 10, 300, 60)
        font = QFont('Times', 14)
        font.setBold(True)
        font.setUnderline(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)
        self.info = QLabel("Welcome", self)
        self.info.setGeometry(40, 85, 260, 60)
        self.info.setWordWrap(True)
        self.info.setFont(QFont('Times', 13))
        self.info.setAlignment(Qt.AlignCenter)
 
        # setting style sheet
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
 
        # creating a spin box to set the number
        self.spin = QSpinBox(self)
        self.spin.setRange(1, 20)
        self.spin.setGeometry(120, 170, 100, 60)
        self.spin.setAlignment(Qt.AlignCenter)
        self.spin.setFont(QFont('Times', 15))
        # creating a push button to check the number
        check = QPushButton("Check", self)
        check.setGeometry(130, 235, 80, 30)
        check.clicked.connect(self.check_action)
        # creating a start button
        start = QPushButton("Start", self)
        start.setGeometry(65, 280, 100, 40)
        # reset button
        reset_game = QPushButton("Reset", self)
        # setting geometry to the push button
        reset_game.setGeometry(175, 280, 100, 40)
        # setting color effect
        color_red = QGraphicsColorizeEffect()
        color_red.setColor(Qt.red)
        reset_game.setGraphicsEffect(color_red)
        color_green = QGraphicsColorizeEffect()
        color_green.setColor(Qt.darkBlue)
        start.setGraphicsEffect(color_green)
        # adding action to the  button
        start.clicked.connect(self.start_action)
        reset_game.clicked.connect(self.reset_action)
 
    def start_action(self):
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
 
        # creating random number
        self.number = random.randint(1, 20)
        self.info.setText("Try to guess number between 1 to 20")
 
 
    def check_action(self):
        # get the spin box number
        user_number = self.spin.value()
        # check the value
        if user_number == self.number:
            self.info.setText("Correct Guess")
            self.info.setStyleSheet("QLabel"
                                    "{"
                                    "border : 2px solid black;"
                                    "background : lightgreen;"
                                    "}")
 
        elif user_number < self.number:
            self.info.setText("Your number is smaller")
 
        else:
            self.info.setText("Your number is larger")
 
 
    def reset_action(self):
        # making label green
        self.info.setStyleSheet("QLabel"
                                "{"
                                "border : 2px solid black;"
                                "background : lightgrey;"
                                "}")
        self.info.setText("Welcome")
 
 
# create pyqt5 app
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
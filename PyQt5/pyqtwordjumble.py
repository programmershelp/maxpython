# import libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # set title
        self.setWindowTitle("Word Jumble")
        self.setGeometry(100, 100, 320, 350)
        self.UiComponents()
        self.show()
        # words
        self.words = ['germany', 'france', 'japan', 'canada', 'spain',
                           'italy', 'mexico', 'brazil', 'china']
        self.current_text = ""
 
    # method for components
    def UiComponents(self):
 
        # creating head label
        head = QLabel("Jumbled Word Game", self)
        head.setGeometry(20, 10, 280, 60)
        # font
        font = QFont('Times', 15)
        font.setBold(True)
        font.setUnderline(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
 
        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)
        self.jumble_word = QLabel(self)
        self.jumble_word.setGeometry(30, 80, 260, 50)
        self.jumble_word.setStyleSheet("border : 2px solid black; background : white;")
        self.jumble_word.setFont(QFont('Times', 12))
        self.jumble_word.setAlignment(Qt.AlignCenter)
        # creating a line edit widget to get the text
        self.input = QLineEdit(self)
        self.input.setGeometry(20, 150, 200, 40)
        self.input.setAlignment(Qt.AlignCenter)
        self.check = QPushButton("Check", self)
        self.check.setGeometry(230, 155, 80, 30)
        # adding action to the check button
        self.check.clicked.connect(self.check_action)
        self.result = QLabel(self)
        self.result.setGeometry(40, 210, 240, 50)
        self.result.setFont(QFont('Times', 13))
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet("border : 2px solid black; background : yellow;")
 
        # creating push buttons to start and reset the game
        start = QPushButton("Start", self)
        reset = QPushButton("Reset", self)
        # setting geometry to the buttons
        start.setGeometry(15, 290, 140, 40)
        reset.setGeometry(165, 290, 140, 40)
        # adding actions to the buttons
        start.clicked.connect(self.start_action)
        reset.clicked.connect(self.reset_action)
 
    def check_action(self):
        text = self.input.text()
        if text == self.current_text:
            self.result.setText("Correct Answer")
            self.result.setStyleSheet("background : lightgreen;")
 
        else:
            self.result.setText("Wrong Answer")
            self.result.setStyleSheet("background : red;")

    def start_action(self):
        # selecting one word
        self.current_text = random.choice(self.words)
        random_word = random.sample(self.current_text, len(self.current_text))
        jumbled = ''.join(random_word)
        self.jumble_word.setText(jumbled)
        self.result.setText("")
        self.result.setStyleSheet("border : 2px solid black; background : yellow;")
        self.input.setText("")
 
    def reset_action(self):
        self.current_text = ""
        self.input.setText("")
        # clear the text of all the labels
        self.jumble_word.setText("")
        self.result.setText("")
        self.result.setStyleSheet("border : 2px solid black; background : yellow;")
 
 
 
# create pyqt5 app
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
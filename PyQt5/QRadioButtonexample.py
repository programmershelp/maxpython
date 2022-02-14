#!/usr/bin/python
from PyQt5.QtWidgets import (QWidget, QRadioButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        radioButton1 = QRadioButton("Python", self)
        radioButton1.toggled.connect(self.updateLabel)

        radioButton2 = QRadioButton("JavaScript", self)
        radioButton2.toggled.connect(self.updateLabel)

        radioButton3 = QRadioButton("CPP", self)
        radioButton3.toggled.connect(self.updateLabel)

        self.label = QLabel('', self)

        hbox.addWidget(radioButton1)
        hbox.addWidget(radioButton2)
        hbox.addWidget(radioButton3)
        
        vbox.addSpacing(10)

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(350, 350, 350, 350)
        self.setWindowTitle('QRadioButton Example')
        self.show()

    def updateLabel(self, value):
        radiobtn = self.sender()
        if radiobtn.isChecked() == True:
            self.label.setText(radiobtn.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
#!/usr/bin/python
from PyQt5.QtWidgets import (QWidget, QRadioButton, QHBoxLayout, QVBoxLayout,
                             QButtonGroup, QLabel, QApplication)
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()

        buttongroup1 = QButtonGroup(self)

        radioButton1 = QRadioButton("Python", self)
        radioButton1.toggled.connect(self.updateLabel1)
        radioButton2 = QRadioButton("JavaScript", self)
        radioButton2.toggled.connect(self.updateLabel1)
        radioButton3 = QRadioButton("CPP", self)
        radioButton3.toggled.connect(self.updateLabel1)


        hbox2 = QHBoxLayout()
        buttongroup2 = QButtonGroup(self)

        radioButton4 = QRadioButton("Windows", self)
        radioButton4.toggled.connect(self.updateLabel2)
        radioButton5 = QRadioButton("Linux", self)
        radioButton5.toggled.connect(self.updateLabel2)
        radioButton6 = QRadioButton("Mac", self)
        radioButton6.toggled.connect(self.updateLabel2)

        self.label1 = QLabel('', self)
        self.label2 = QLabel('', self)

        buttongroup1.addButton(radioButton1)
        buttongroup1.addButton(radioButton2)
        buttongroup1.addButton(radioButton3)

        buttongroup2.addButton(radioButton4)
        buttongroup2.addButton(radioButton5)
        buttongroup2.addButton(radioButton6)

        hbox1.addWidget(radioButton1)
        hbox1.addWidget(radioButton2)
        hbox1.addWidget(radioButton3)

        hbox2.addWidget(radioButton4)
        hbox2.addWidget(radioButton5)
        hbox2.addWidget(radioButton6)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QRadioButton')
        self.show()

    def updateLabel1(self, value):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label1.setText(rbtn.text())

    def updateLabel2(self, value):
        rbtn = self.sender()
        if rbtn.isChecked() == True:
            self.label2.setText(rbtn.text())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
from PyQt5.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        checkBox1 = QCheckBox('Change title', self)
        checkBox1.toggle()
        checkBox1.stateChanged.connect(self.changeTitle)

        hbox.addWidget(checkBox1)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QCheckBox Example')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Checkbox checked')
        else:
            self.setWindowTitle('Checkbox not checked')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
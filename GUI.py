"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from amazonfc import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 thing'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # lbl1 = QLabel('Zetcode', self)
        # lbl1.move(15, 10)

        # lbl2 = QLabel('tutorials', self)
        # lbl2.move(35, 40)

        # lbl3 = QLabel('for programmers', self)
        # lbl3.move(55, 70)

        # okButton = QPushButton("OK")
        # cancelButton = QPushButton("Cancel")

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(okButton)
        # hbox.addWidget(cancelButton)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)

        # grid = QGridLayout()
        # self.setLayout(grid)

        # names = ['Cls', 'Bck', '', 'Close',
        #          '7', '8', '9', '/',
        #         '4', '5', '6', '*',
        #          '1', '2', '3', '-',
        #         '0', '.', '=', '+']

        # positions = [(i,j) for i in range(5) for j in range(4)]

        # for position, name in zip(positions, names):

        #     if name == '':
        #         continue
        #     button = QPushButton(name)
        #     grid.addWidget(button, *position)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()

        # self.show()
        # self.getInteger()
        # self.getText()
        # self.getDouble()
        # self.getChoice()

        self.show()

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer", "Percentage:",
                                           28, 0, 100, 1)
        if okPressed:
            print(i)

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Get double", "Value:",
                                              10.50, 0, 100, 10)
        if okPressed:
            print(d)

    def getChoice(self):
        items = ("Red", "Blue", "Green")
        item, okPressed = QInputDialog.getItem(self, "Get item", "Color:",
                                               items, 0, False)
        if okPressed and item:
            print(item)

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text", "Your name:",
                                               QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
"""

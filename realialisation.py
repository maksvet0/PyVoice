import os
import gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class App(QMainWindow, gui.Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        super(App, self)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(lambda: self.OnClick())
    def OnClick(self):
        print("111")
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    apl = App()
    apl.show()
    apl.show()
    apl.exec()


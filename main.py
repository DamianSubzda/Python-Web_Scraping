# Damian Subzda
# WCY19IJ3S1

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from windowM import Ui_MainWindow
from thread import Thread

thread1 = Thread()
thread1.start()

def close():
    app.exec_()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setup(MainWindow)
MainWindow.show()
sys.exit(close())












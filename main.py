# Damian Subzda
# WCY19IJ3S1
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

import windowM
import info
from windowM import Ui_MainWindow
from thread import Thread

thread1 = Thread()
thread1.start()

#Ui_MainWindow.start(windowM.Ui_MainWindow)
#info.Ui_Info.start(info.Ui_Info)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setup(MainWindow)
MainWindow.show()
sys.exit(app.exec_())












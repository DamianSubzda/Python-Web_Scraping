# Damian Subzda
# WCY19IJ3S1
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

import windowM
from windowM import Ui_MainWindow
from thread import Thread

thread1 = Thread()
thread1.start()

Ui_MainWindow.start(windowM.Ui_MainWindow)












# Damian Subzda WCY19IJ3S1

from PyQt5 import QtCore, QtGui, QtWidgets
import windowM
from thread import thread

thread1 = thread()
thread1.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = windowM.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





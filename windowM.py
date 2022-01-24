# Damian Subzda
# WCY19IJ3S1

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 571)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Search.setGeometry(QtCore.QRect(630, 110, 101, 31))
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 441, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_Currency = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Currency.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.comboBox_Currency.setObjectName("comboBox_Currency")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(170, 200, 441, 321))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_Copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Copy.setGeometry(QtCore.QRect(630, 490, 131, 31))
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(610, 10, 131, 51))
        self.label1.setObjectName("label1")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(170, 160, 191, 31))
        self.label3.setObjectName("label3")
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setGeometry(QtCore.QRect(630, 450, 131, 31))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.label2.setObjectName("label2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))
        self.pushButton_Copy.setText(_translate("MainWindow", "Copy To Clipboard"))
        self.label1.setText(_translate("MainWindow", "Number of elements:"))
        self.label3.setText(_translate("MainWindow", "Sorted by lowest price:"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open in browser"))
        self.label2.setText(_translate("MainWindow", "Search in database:"))


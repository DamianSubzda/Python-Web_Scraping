# Damian Subzda
# WCY19IJ3S1

#TODO Możliwość dodania dwóch rzeczy do porównania (dodanie w osobnym okienku)
#TODO Dodanie do listy wszystkich wyszukanych aby móc wyjąć z niej href'a
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem

import DataBaseConnection
import sys

class Ui_MainWindow():

    def __init__(self):
        pass

    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setup(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 571)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(630, 50, 101, 31))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.pushButton_Refresh.clicked.connect(self.refreshClick)

        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Search.setGeometry(QtCore.QRect(630, 110, 101, 31))
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.pushButton_Search.clicked.connect(self.searchClick)

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

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(510, 10, 231, 71))
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.adjustSize()
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(170, 160, 191, 31))
        self.label3.setObjectName("label3")
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setGeometry(QtCore.QRect(630, 450, 131, 31))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton_Open.clicked.connect(self.openBrowser)


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(170, 70, 191, 31))
        self.label2.setObjectName("label2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def refreshClick(self):
        self.label1.setText(f"Number of elements:{DataBaseConnection.DataBaseConnector.idOfItems}")
        self.label1.adjustSize()

    def searchClick(self):
        self.delateItemsFromList()
        temp = self.lineEdit.text()
        if temp != "":
            rows = DataBaseConnection.DataBaseConnector.getRecords(DataBaseConnection.DataBaseConnector, temp)
            #print(rows)
            for row in rows:
                temp2 = str(row[0])+ ": Price: " + str(row[2]) + " " + str(row[3]) + "\tTitle: " + str(row[1])
                print(temp2)
                self.listWidget.addItem(temp2)

        self.lineEdit.setText("")

    def delateItemsFromList(self):
        self.listWidget.clear()

    def openBrowser(self):
        webbrowser.open("https://google.com")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))
        self.pushButton_Copy.setText(_translate("MainWindow", "Copy To Clipboard"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.label1.setText(f"Number of elements:{DataBaseConnection.DataBaseConnector.idOfItems}")
        self.label1.adjustSize()
        self.label3.setText(_translate("MainWindow", "Sorted by lowest price:"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open in browser"))
        self.label2.setText(_translate("MainWindow", "Search in database:"))


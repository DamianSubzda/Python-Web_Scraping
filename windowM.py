# Damian Subzda
# WCY19IJ3S1

#TODO Możliwość dodania dwóch rzeczy do porównania (dodanie w osobnym okienku)

import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QApplication

import DataBaseConnection
import info
import element

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.popups = []

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

        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setGeometry(QtCore.QRect(630, 370, 50, 31))
        self.pushButton_Add.setObjectName("pushButton_Add")
        #self.pushButton_Add.clicked.connect(self.searchClick)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 441, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(170, 200, 441, 321))
        self.listWidget.setObjectName("listWidget")

        self.pushButton_Copy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Copy.setGeometry(QtCore.QRect(630, 490, 131, 31))
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.pushButton_Copy.clicked.connect(self.copyToClipboard)

        self.pushButton_Info = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Info.setGeometry(QtCore.QRect(630, 410, 131, 31))
        self.pushButton_Info.setObjectName("pushButton_Info")
        self.pushButton_Info.clicked.connect(self.showInfo)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(510, 10, 231, 71))
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.adjustSize()

        font.setPointSize(10)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(170, 160, 191, 31))
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setGeometry(QtCore.QRect(630, 450, 131, 31))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton_Open.clicked.connect(self.openBrowser)


        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font.setPointSize(10)
        self.label2.setFont(font)
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

    def showInfo(self):

        x = self.listWidget.selectedItems()
        if len(x)==0:
            pass
        else:
            for y in x:
                x = y.text()
            id = int(self.getID(x))
            row = DataBaseConnection.DataBaseConnector.getRecordByID(DataBaseConnection.DataBaseConnector, id)
            popWin = info.Ui_Info(row)
            popWin.show()
            self.popups.append(popWin)

    def refreshClick(self):
        self.label1.setText(f"Number of elements:{DataBaseConnection.DataBaseConnector.idOfItems}")
        self.label1.adjustSize()

    def searchClick(self):
        self.delateItemsFromList()
        temp = self.lineEdit.text()
        if temp != "":
            rows = DataBaseConnection.DataBaseConnector.getRecords(DataBaseConnection.DataBaseConnector, temp)
            for row in rows:
                temp2 = str(row[0])+ ": Price:  " + str(row[2]) + " " + str(row[3]) + "\tTitle:  " + str(row[1])
                self.listWidget.addItem(temp2)

        self.lineEdit.setText("")

    def copyToClipboard(self):

        x = self.listWidget.selectedItems()
        if len(x)==0:
            pass
        else:
            for y in x:
                x = y.text()
            id = int(self.getID(x))
            row = DataBaseConnection.DataBaseConnector.getRecordByID(DataBaseConnection.DataBaseConnector, id)
            href = row[8]
            clipboard = QApplication.clipboard()
            clipboard.clear(mode=clipboard.Clipboard)
            clipboard.setText(f"https://www.discogs.com{href}", mode=clipboard.Clipboard)

    def getID(self, text):
        if text[1] == ':':
            return text[:1]
        elif text[2] == ':':
            return text[:2]
        elif text[3] == ':':
            return text[:3]
        elif text[4] == ':':
            return text[:4]
        else:
            return 0

    def delateItemsFromList(self):
        self.listWidget.clear()

    def openBrowser(self):
        x = self.listWidget.selectedItems()
        if len(x) == 0:
            pass
        else:
            for y in x:
                x = y.text()
            id = int(self.getID(x))
            row = DataBaseConnection.DataBaseConnector.getRecordByID(DataBaseConnection.DataBaseConnector, id)
            href = row[8]

            webbrowser.open(f"https://www.discogs.com{href}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comparison engine"))
        self.pushButton_Search.setText(_translate("MainWindow", "Search"))
        self.pushButton_Copy.setText(_translate("MainWindow", "Copy To Clipboard"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_Info.setText(_translate("MainWindow", "Show more info"))
        self.label1.setText(f"Number of elements:{DataBaseConnection.DataBaseConnector.idOfItems}")
        self.label1.adjustSize()
        self.label3.setText(_translate("MainWindow", "List of elements :"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open in browser"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.label2.setText(_translate("MainWindow", "Search in database:"))


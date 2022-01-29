import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        super(Ui_Info, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(443, 285)
        self.label_title = QtWidgets.QLabel(Info)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_original_price = QtWidgets.QLabel(Info)
        self.label_original_price.setGeometry(QtCore.QRect(10, 50, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_original_price.setFont(font)
        self.label_original_price.setObjectName("label_original_price")
        self.label_rating = QtWidgets.QLabel(Info)
        self.label_rating.setGeometry(QtCore.QRect(10, 90, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_rating.setFont(font)
        self.label_rating.setObjectName("label_rating")
        self.label_have = QtWidgets.QLabel(Info)
        self.label_have.setGeometry(QtCore.QRect(10, 130, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_have.setFont(font)
        self.label_have.setObjectName("label_have")
        self.label_want = QtWidgets.QLabel(Info)
        self.label_want.setGeometry(QtCore.QRect(10, 170, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_want.setFont(font)
        self.label_want.setObjectName("label_want")
        self.label_price = QtWidgets.QLabel(Info)
        self.label_price.setGeometry(QtCore.QRect(140, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")
        self.comboBox = QtWidgets.QComboBox(Info)
        self.comboBox.setGeometry(QtCore.QRect(10, 220, 111, 31))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info"))
        self.label_title.setText(_translate("Info", "Title:"))
        self.label_original_price.setText(_translate("Info", "Original price:"))
        self.label_rating.setText(_translate("Info", "Rating:"))
        self.label_have.setText(_translate("Info", "Have:"))
        self.label_want.setText(_translate("Info", "Want:"))
        self.label_price.setText(_translate("Info", "Price in $ :"))


# Damian Subzda
# WCY19IJ3S1

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Comparison(object):
    def setupUi(self, Comparison):
        Comparison.setObjectName("Comparison")
        Comparison.resize(630, 525)
        self.line = QtWidgets.QFrame(Comparison)
        self.line.setGeometry(QtCore.QRect(0, 65, 630, 20))
        self.line.setBaseSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Comparison)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 630, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Comparison)
        self.line_3.setGeometry(QtCore.QRect(0, 215, 630, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Comparison)
        self.line_4.setGeometry(QtCore.QRect(0, 290, 630, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Comparison)
        self.line_5.setGeometry(QtCore.QRect(0, 365, 630, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Comparison)
        self.line_6.setGeometry(QtCore.QRect(0, 440, 630, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Comparison)
        self.line_7.setGeometry(QtCore.QRect(250, 0, 20, 531))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Comparison)
        self.line_8.setGeometry(QtCore.QRect(380, 0, 20, 531))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayoutWidget = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 261, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1_1.setObjectName("label_1_1")
        self.gridLayout.addWidget(self.label_1_1, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(390, 0, 241, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2_1.setObjectName("label_2_1")
        self.gridLayout_2.addWidget(self.label_2_1, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(390, 80, 241, 71))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2_2.setObjectName("label_2_2")
        self.gridLayout_3.addWidget(self.label_2_2, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(390, 150, 241, 71))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_2_3.setObjectName("label_2_3")
        self.gridLayout_4.addWidget(self.label_2_3, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(390, 230, 241, 71))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_2_4.setObjectName("label_2_4")
        self.gridLayout_5.addWidget(self.label_2_4, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(390, 300, 241, 71))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2_5 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.label_2_5.setObjectName("label_2_5")
        self.gridLayout_6.addWidget(self.label_2_5, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(390, 380, 241, 71))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_2_6 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_2_6.setObjectName("label_2_6")
        self.gridLayout_7.addWidget(self.label_2_6, 0, 0, 1, 1)
        self.gridLayoutWidget_8 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(390, 450, 241, 71))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2_7 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_2_7.setObjectName("label_2_7")
        self.gridLayout_8.addWidget(self.label_2_7, 0, 0, 1, 1)
        self.gridLayoutWidget_9 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(0, 80, 261, 71))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_1_2 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_1_2.setObjectName("label_1_2")
        self.gridLayout_9.addWidget(self.label_1_2, 0, 0, 1, 1)
        self.gridLayoutWidget_10 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(0, 150, 261, 71))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_1_3 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_1_3.setObjectName("label_1_3")
        self.gridLayout_10.addWidget(self.label_1_3, 0, 0, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(0, 230, 261, 71))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_1_4 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_1_4.setObjectName("label_1_4")
        self.gridLayout_11.addWidget(self.label_1_4, 0, 0, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(0, 300, 261, 71))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_1_5 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_1_5.setObjectName("label_1_5")
        self.gridLayout_12.addWidget(self.label_1_5, 0, 0, 1, 1)
        self.gridLayoutWidget_13 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_13.setGeometry(QtCore.QRect(0, 380, 261, 71))
        self.gridLayoutWidget_13.setObjectName("gridLayoutWidget_13")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_1_6 = QtWidgets.QLabel(self.gridLayoutWidget_13)
        self.label_1_6.setObjectName("label_1_6")
        self.gridLayout_13.addWidget(self.label_1_6, 0, 0, 1, 1)
        self.gridLayoutWidget_14 = QtWidgets.QWidget(Comparison)
        self.gridLayoutWidget_14.setGeometry(QtCore.QRect(0, 450, 261, 71))
        self.gridLayoutWidget_14.setObjectName("gridLayoutWidget_14")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.gridLayoutWidget_14)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_1_7 = QtWidgets.QLabel(self.gridLayoutWidget_14)
        self.label_1_7.setObjectName("label_1_7")
        self.gridLayout_14.addWidget(self.label_1_7, 0, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(Comparison)
        self.label_title.setGeometry(QtCore.QRect(260, 30, 131, 20))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_label = QtWidgets.QLabel(Comparison)
        self.label_label.setGeometry(QtCore.QRect(260, 100, 131, 20))
        self.label_label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_label.setObjectName("label_label")
        self.label_rating = QtWidgets.QLabel(Comparison)
        self.label_rating.setGeometry(QtCore.QRect(260, 180, 131, 20))
        self.label_rating.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rating.setObjectName("label_rating")
        self.label_have = QtWidgets.QLabel(Comparison)
        self.label_have.setGeometry(QtCore.QRect(260, 250, 131, 20))
        self.label_have.setAlignment(QtCore.Qt.AlignCenter)
        self.label_have.setObjectName("label_have")
        self.label_want = QtWidgets.QLabel(Comparison)
        self.label_want.setGeometry(QtCore.QRect(260, 330, 131, 20))
        self.label_want.setAlignment(QtCore.Qt.AlignCenter)
        self.label_want.setObjectName("label_want")
        self.label_price = QtWidgets.QLabel(Comparison)
        self.label_price.setGeometry(QtCore.QRect(260, 400, 131, 20))
        self.label_price.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price.setObjectName("label_price")
        self.label_priceIn = QtWidgets.QLabel(Comparison)
        self.label_priceIn.setGeometry(QtCore.QRect(260, 460, 131, 20))
        self.label_priceIn.setAlignment(QtCore.Qt.AlignCenter)
        self.label_priceIn.setObjectName("label_priceIn")
        self.comboBox = QtWidgets.QComboBox(Comparison)
        self.comboBox.setGeometry(QtCore.QRect(290, 490, 73, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Comparison)
        QtCore.QMetaObject.connectSlotsByName(Comparison)

    def retranslateUi(self, Comparison):
        _translate = QtCore.QCoreApplication.translate
        Comparison.setWindowTitle(_translate("Comparison", "Comparison"))
        self.label_1_1.setText(_translate("Comparison", "TextLabel"))
        self.label_2_1.setText(_translate("Comparison", "TextLabel"))
        self.label_2_2.setText(_translate("Comparison", "TextLabel"))
        self.label_2_3.setText(_translate("Comparison", "TextLabel"))
        self.label_2_4.setText(_translate("Comparison", "TextLabel"))
        self.label_2_5.setText(_translate("Comparison", "TextLabel"))
        self.label_2_6.setText(_translate("Comparison", "TextLabel"))
        self.label_2_7.setText(_translate("Comparison", "TextLabel"))
        self.label_1_2.setText(_translate("Comparison", "TextLabel"))
        self.label_1_3.setText(_translate("Comparison", "TextLabel"))
        self.label_1_4.setText(_translate("Comparison", "TextLabel"))
        self.label_1_5.setText(_translate("Comparison", "TextLabel"))
        self.label_1_6.setText(_translate("Comparison", "TextLabel"))
        self.label_1_7.setText(_translate("Comparison", "TextLabel"))
        self.label_title.setText(_translate("Comparison", "Title"))
        self.label_label.setText(_translate("Comparison", "Label"))
        self.label_rating.setText(_translate("Comparison", "Rating"))
        self.label_have.setText(_translate("Comparison", "Have"))
        self.label_want.setText(_translate("Comparison", "Want"))
        self.label_price.setText(_translate("Comparison", "Price"))
        self.label_priceIn.setText(_translate("Comparison", "Price in $"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Comparison = QtWidgets.QWidget()
    ui = Ui_Comparison()
    ui.setupUi(Comparison)
    Comparison.show()
    sys.exit(app.exec_())

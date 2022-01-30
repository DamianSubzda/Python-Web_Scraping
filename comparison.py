# Damian Subzda
# WCY19IJ3S1

from PyQt5 import QtCore, QtGui, QtWidgets
import windowM

class Ui_Comparison(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_Comparison, self).__init__(parent)
        self.setupUi(self)
        self.setColors()

    def setupUi(self, Comparison):

        Comparison.setObjectName("Comparison")
        Comparison.resize(630, 613)
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
        self.comboBox.addItem("$")
        self.comboBox.addItem("¥")
        self.comboBox.addItem("CHF")
        self.comboBox.addItem("SEK")
        self.comboBox.addItem("CA$")
        self.comboBox.addItem("ZAR")
        self.comboBox.addItem("MX$")
        self.comboBox.addItem("NZ$")
        self.comboBox.addItem("R$")
        self.comboBox.addItem("A$")
        self.comboBox.addItem("€")
        self.comboBox.addItem("£")
        font = self.comboBox.font()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.currentTextChanged.connect(self.setCurrency)

        self.label_title_1 = QtWidgets.QLabel(Comparison)
        self.label_title_1.setGeometry(QtCore.QRect(-2, 0, 261, 75))
        self.label_title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_1.setObjectName("label_title_1")
        self.line_9 = QtWidgets.QFrame(Comparison)
        self.line_9.setGeometry(QtCore.QRect(0, 520, 630, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_1 = QtWidgets.QLabel(Comparison)
        self.label_1.setGeometry(QtCore.QRect(260, 540, 131, 41))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_title_2 = QtWidgets.QLabel(Comparison)
        self.label_title_2.setGeometry(QtCore.QRect(390, 0, 241, 75))
        self.label_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.label_label_2 = QtWidgets.QLabel(Comparison)
        self.label_label_2.setGeometry(QtCore.QRect(390, 75, 241, 75))
        self.label_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_label_2.setObjectName("label_label_2")
        self.label_label_1 = QtWidgets.QLabel(Comparison)
        self.label_label_1.setGeometry(QtCore.QRect(0, 75, 261, 75))
        self.label_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_label_1.setObjectName("label_label_1")
        self.label_rating_1 = QtWidgets.QLabel(Comparison)
        self.label_rating_1.setGeometry(QtCore.QRect(0, 150, 261, 75))
        self.label_rating_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rating_1.setObjectName("label_rating_1")
        self.label_have_1 = QtWidgets.QLabel(Comparison)
        self.label_have_1.setGeometry(QtCore.QRect(0, 225, 261, 75))
        self.label_have_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_have_1.setObjectName("label_have_1")
        self.label_want_1 = QtWidgets.QLabel(Comparison)
        self.label_want_1.setGeometry(QtCore.QRect(0, 300, 261, 75))
        self.label_want_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_want_1.setObjectName("label_want_1")
        self.label_price_1 = QtWidgets.QLabel(Comparison)
        self.label_price_1.setGeometry(QtCore.QRect(0, 375, 261, 75))
        self.label_price_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price_1.setObjectName("label_price_1")
        self.label_priceIn_1 = QtWidgets.QLabel(Comparison)
        self.label_priceIn_1.setGeometry(QtCore.QRect(0, 450, 261, 75))
        self.label_priceIn_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_priceIn_1.setObjectName("label_priceIn_1")
        self.label_rating_2 = QtWidgets.QLabel(Comparison)
        self.label_rating_2.setGeometry(QtCore.QRect(390, 150, 241, 75))
        self.label_rating_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rating_2.setObjectName("label_rating_2")
        self.label_have_2 = QtWidgets.QLabel(Comparison)
        self.label_have_2.setGeometry(QtCore.QRect(390, 225, 241, 75))
        self.label_have_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_have_2.setObjectName("label_have_2")
        self.label_want_2 = QtWidgets.QLabel(Comparison)
        self.label_want_2.setGeometry(QtCore.QRect(390, 300, 241, 75))
        self.label_want_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_want_2.setObjectName("label_want_2")
        self.label_price_2 = QtWidgets.QLabel(Comparison)
        self.label_price_2.setGeometry(QtCore.QRect(390, 375, 241, 75))
        self.label_price_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_price_2.setObjectName("label_price_2")
        self.label_priceIn_2 = QtWidgets.QLabel(Comparison)
        self.label_priceIn_2.setGeometry(QtCore.QRect(390, 450, 241, 75))
        self.label_priceIn_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_priceIn_2.setObjectName("label_priceIn_2")
        self.checkBox_1 = QtWidgets.QCheckBox(Comparison)
        self.checkBox_1.setGeometry(QtCore.QRect(240, 550, 21, 20))
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(Comparison)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 550, 21, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Comparison)
        QtCore.QMetaObject.connectSlotsByName(Comparison)

        self.label_title_1.setWordWrap(True)
        self.label_title_2.setWordWrap(True)
        self.label_label_1.setWordWrap(True)
        self.label_label_2.setWordWrap(True)

    def setColors(self):

        if int(self.label_have_1.text()) > int(self.label_have_2.text()):
            self.label_have_1.setStyleSheet("background-color: rgb(8, 204, 93)")
            self.label_have_2.setStyleSheet("background-color: rgb(189, 53, 0)")
        elif int(self.label_have_1.text()) < int(self.label_have_2.text()):
            self.label_have_2.setStyleSheet("background-color: rgb(8, 204, 93)")
            self.label_have_1.setStyleSheet("background-color: rgb(189, 53, 0)")
        else:
            self.label_have_2.setStyleSheet("background-color: rgb(99, 89, 86)")
            self.label_have_1.setStyleSheet("background-color: rgb(99, 89, 86)")

        if int(self.label_want_1.text()) > int(self.label_want_2.text()):
            self.label_want_1.setStyleSheet("background-color: rgb(8, 204, 93)")
            self.label_want_2.setStyleSheet("background-color: rgb(189, 53, 0)")
        elif int(self.label_want_1.text()) < int(self.label_want_2.text()):
            self.label_want_2.setStyleSheet("background-color: rgb(8, 204, 93)")
            self.label_want_1.setStyleSheet("background-color: rgb(189, 53, 0)")
        else:
            self.label_want_2.setStyleSheet("background-color: rgb(99, 89, 86)")
            self.label_want_1.setStyleSheet("background-color: rgb(99, 89, 86)")

    def setCurrency(self):
        currency = self.currencyComboBox
        price = self.priceComboBox
        if currency == '$':
            price = price
        elif currency == '¥':
            price = float(price * 0.0087)
        elif currency == "CHF":
            price = float(price * 1.07)
        elif currency == "SEK":
            price = float(price * 0.11)
        elif currency == "CA$":
            price = float(price * 0.78)
        elif currency == "ZAR":
            price = float(price * 0.064)
        elif currency == "MX$":
            price = float(price * 0.048)
        elif currency == "NZ$":
            price = float(price * 0.653971)
        elif currency == "R$":
            price = float(price * 0.186)
        elif currency == "A$":
            price = float(price * 0.699)
        elif currency == "€":
            price = float(price * 1.11)
        elif currency == "£":
            price = float(price * 1.34)
        else:
            print("Nowa waluta:" + price)
            price = 0

        currency = self.comboBox.currentText()

        if currency == '$':
            price = price
        elif currency == '¥':
            price = float(price * 115.22)
        elif currency == "CHF":
            price = float(price * 0.93)
        elif currency == "SEK":
            price = float(price * 9.41)
        elif currency == "CA$":
            price = float(price * 1.27)
        elif currency == "ZAR":
            price = float(price * 15.59)
        elif currency == "MX$":
            price = float(price * 20.79)
        elif currency == "NZ$":
            price = float(price * 1.52)
        elif currency == "R$":
            price = float(price * 5.36)
        elif currency == "A$":
            price = float(price * 1.43)
        elif currency == "€":
            price = float(price * 0.90)
        elif currency == "£":
            price = float(price * 0.75)
        else:
            print("Nowa waluta:" + price)
            price = 0
        #self.label_price.setText(f"Price in {currency}: {round(price, 2)}")

    def retranslateUi(self, Comparison):
        _translate = QtCore.QCoreApplication.translate
        Comparison.setWindowTitle(_translate("Comparison", "Comparison"))
        self.label_title.setText(_translate("Comparison", "Title"))
        self.label_label.setText(_translate("Comparison", "Label"))
        self.label_rating.setText(_translate("Comparison", "Rating"))
        self.label_have.setText(_translate("Comparison", "Have"))
        self.label_want.setText(_translate("Comparison", "Want"))
        self.label_price.setText(_translate("Comparison", "Price"))
        self.label_1.setText(_translate("Comparison", "<- Remember ->"))
        self.label_title_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][1]}"))
        self.label_title_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][1]}"))
        self.label_label_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][2]}"))
        self.label_label_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][2]}"))
        self.label_rating_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][5]}"))
        self.label_rating_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][5]}"))
        self.label_have_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][6]}"))
        self.label_want_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][7]}"))
        self.label_have_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][6]}"))
        self.label_want_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][7]}"))
        self.label_price_1.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[0][2]}{windowM.Ui_MainWindow.elements[0][3]}"))
        self.label_price_2.setText(_translate("Comparison", f"{windowM.Ui_MainWindow.elements[1][2]}{windowM.Ui_MainWindow.elements[1][3]}"))
        self.label_priceIn_1.setText(_translate("Comparison", "Comming soon"))
        self.label_priceIn.setText(_translate("Comparison", "Price in $"))
        self.label_priceIn_2.setText(_translate("Comparison", "TextLabel"))



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info(QtWidgets.QMainWindow):

    def __init__(self,row, parent=None):
        super(Ui_Info, self).__init__(parent)
        self.setupUi(self)
        self.setLabels(row)
        self.currencyComboBox = "$"
        self.priceComboBox = row[2]
        self.element1 = None
        self.element2 = None

    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(550, 285)
        self.label_title = QtWidgets.QLabel(Info)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 1501, 31))
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
        self.label_price.setGeometry(QtCore.QRect(150, 220, 350, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_price.setFont(font)
        self.label_price.setObjectName("label_price")

        self.comboBox = QtWidgets.QComboBox(Info)
        self.comboBox.setGeometry(QtCore.QRect(10, 220, 111, 31))
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
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.currentTextChanged.connect(self.setCurrency)
        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

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
        self.label_price.setText(f"Price in {currency}: {round(price, 2)}")

    def setLabels(self, row):
        self.label_title.setText(f"Title: {row[1]}")
        self.label_original_price.setText(f"Original price: {row[2]}{row[3]}")
        self.label_rating.setText(f"Rating: {row[5]}")
        self.label_have.setText(f"Have: {row[6]}")
        self.label_want.setText(f"Want: {row[7]}")
        self.label_price.setText("<- Select currency")

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Info"))
        self.label_title.setText(_translate("Info", "Title:"))
        self.label_original_price.setText(_translate("Info", "Original price:"))
        self.label_rating.setText(_translate("Info", "Rating:"))
        self.label_have.setText(_translate("Info", "Have:"))
        self.label_want.setText(_translate("Info", "Want:"))
        self.label_price.setText(_translate("Info", "Price in $ :"))


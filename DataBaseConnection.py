# Damian Subzda
# WCY19IJ3S1
from Demos.win32gui_menu import MainWindow
from PyQt5.uic.properties import QtWidgets
from bs4 import BeautifulSoup
from requests import get
import sqlite3
from sys import argv

class DataBaseConnector():

    idOfItems = 0

    def __init__(self, idOfItems):
        self.idOfItems = idOfItems

    def haveWant(self, shortcut):
        shortcutNum = shortcut.find_all('div', class_="community_result")
        want = 0
        have = 0
        if (len(shortcutNum) == 2):
            have = int(shortcut.find_all('span', class_="community_number")[0].get_text())
            want = int(shortcut.find_all('span', class_="community_number")[1].get_text())
            pass
        elif (len(shortcutNum) == 1):
            temp = shortcut.find_all('span', class_="community_label")[0].get_text()
            if (temp[2:] == "want"):
                want = int(temp[:-5])
                have = 0
            else:
                have = int(temp[:-5])
                want = 0
        else:
            pass
        return have, want

    def ParsePage(self, nextPage):
        page = get(f'{URL}&page={nextPage}')
        bs = BeautifulSoup(page.content, "html.parser")
        if bs.find('h1').get_text() == "404! Oh no!":
            return False
        else:
            for shortcut in bs.find_all('tr', class_="shortcut_navigable"):

                self.idOfItems = self.idOfItems + 1
                title = shortcut.find('a', class_="item_description_title").get_text()  # [:-10]
                labelShortcut = shortcut.find('p', class_="hide_mobile label_and_cat")
                label = labelShortcut.find('a').get_text()
                shipFromShortcut = shortcut.find_all('li')
                if shipFromShortcut[1].find('span', class_="muted"):
                    star_rating = "0.0%"
                else:
                    star_rating = shipFromShortcut[1].find('strong').get_text()
                have, want = self.haveWant(self, shortcut)
                price = shortcut.find('span', class_="price").get_text()
                price, currency = self.splitCurrency(self, price)
                cursor.execute('INSERT INTO dane VALUES (?, ?,?,?,?,?,?,?)',
                               (self.idOfItems, title, price, currency, label, star_rating, have, want))
                conn.commit()
        return True

    def WebScraper(self):
        global URL, conn, cursor, haveWant, splitCurrency
        URL = 'https://www.discogs.com/sell/list?sort=title%2Casc&limit=25'
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        if len(argv) > 1:
            cursor.execute(
                '''CREATE TABLE dane (id INTEGER,title TEXT,price REAL,currency TEXT, label TEXT, star_rating TEXT, have INTEGER, want INTEGER )''')
            quit()

        cursor.execute('''DELETE FROM dane''')

        #ParsePage(1)

        for i in range(1, 20):
            self.ParsePage(self, i)
            print("i: " + str(i))

        '''
        #Przechodzi po wszystkich stronach
        x = True
        i = 1
        while x == True:
            x = ParsePage(i)
            i +=1
        '''
        conn.close()

    def splitCurrency(self, price):
        price = price.replace(',', '')
        if price[:1] == '$':
            currency = '$'
            price = float(price[1:])
            return price, currency
        elif price[:1] == '¥':
            currency = '¥'
            price = float(price[1:])
            return price, currency
        elif price[:3] == "CHF":
            currency = 'CHF'
            price = float(price[3:])
            return price, currency
        elif price[:3] == "SEK":
            currency = 'SEK'
            price = float(price[3:])
            return price, currency
        elif price[:3] == "CA$":
            currency = 'CA$'
            price = float(price[3:])
            return price, currency
        elif price[:3] == "ZAR":
            currency = 'ZAR'
            price = float(price[3:])
            return price, currency
        elif price[:3] == "MX$":
            currency = 'MX$'
            price = float(price[3:])
            return price, currency
        elif price[:3] == "NZ$":
            currency = 'MX$'
            price = float(price[3:])
            return price, currency
        elif price[:2] == "R$":
            currency = 'R$'
            price = float(price[2:])
            return price, currency
        elif price[:2] == "A$":
            currency = 'A$'
            price = float(price[2:])
            return price, currency
        elif price[:1] == "€":
            currency = '€'
            price = float(price[1:])
            return price, currency
        elif price[:1] == "£":
            currency = '£'
            price = float(price[1:])
            return price, currency
        else:
            print("Nowa waluta:" + price)
            return price, price

        return price, currency

    def GetAmountOfItems(self):
        return self.idOfItems

#Po nazwie porówywanie
#Patrzenie czy się zmieniło w czasie (od ostatniego czasu)
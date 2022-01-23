# Damian Subzda WCY19IJ3S1
import threading
from tkinter import *

import DataBaseConnection
import window

class thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        DataBaseConnection.WebScraper()
        pass


thread1 = thread(1)
thread1.start()

desktopApp = Tk()
desktopApp.geometry('800x500')
desktopApp.title("Porównywarka")


def close():
    pass

def ReadRowFromDB():
    pass

def DisplayDataOnScrean():
    pass

def Accept(event):
    print("Wcisniety przycisk")

def Refresh(event):
    amountOfRows = Label(desktopApp, text=DataBaseConnection.GetAmountOfItems())
    amountOfRows.pack()


def ShowFirstSkreen():
    pickByIDText1 = Label(desktopApp, text="Wybierz rzecz do porównania(ID) 1: ", bg="#aebdb2", height=2)
    pickByIDText1.pack(padx=10, pady=10, expand=TRUE, anchor=NW)
    pickByIDText2 = Label(desktopApp, text="Wybierz rzecz do porównania(ID) 2: ", bg="#aebdb2", height=2)
    pickByIDText2.pack(padx=10, expand=TRUE, anchor=NW)
    buttonAccept = Button(text="Zatwierdz");
    buttonAccept.pack(expand=TRUE)
    amountOfRows = Label(desktopApp, text=DataBaseConnection.GetAmountOfItems())
    amountOfRows.pack()

    buttonRefresh = Button(text = "Odśwież")
    buttonRefresh.pack(expand=TRUE, anchor = NE)

    buttonRefresh.bind("<ButtonRelease>", Refresh)
    buttonAccept.bind("<ButtonRelease>", Accept)

#ShowFirstSkreen()
window.window()

desktopApp.mainloop()

#thread1.join()


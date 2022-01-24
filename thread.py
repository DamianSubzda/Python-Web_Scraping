
import threading

import DataBaseConnection


class thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        DataBaseConnection.WebScraper()
        pass
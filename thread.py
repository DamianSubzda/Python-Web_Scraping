# Damian Subzda
# WCY19IJ3S1

import threading
import DataBaseConnection

class Thread(threading.Thread):
    def __init__(self,  *args, **kwargs):
        super(Thread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def run(self):
        DataBaseConnection.DataBaseConnector.WebScraper(DataBaseConnection.DataBaseConnector)

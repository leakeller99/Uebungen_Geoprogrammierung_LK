from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse 

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Uebungen_Geoprogrammierung/6_Uebung_LK.ui", self)

        self.pushButton.clicked.connect(self.karte)

    def karte(self):
        laenge = self.Laenge.text()
        breite = self.Breite.text()
        link = f"https://www.google.ch/maps/place/{breite},{laenge}"
        QDesktopServices.openUrl(QUrl(link))

app = QApplication([])
window = Fenster()
window.show()

app.exec()
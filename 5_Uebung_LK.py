import sys
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
import urllib.parse 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")
        
        layout = QFormLayout()

        # Widget-Instanzen erstellen:
        self.vornameLineEdit = QLineEdit()
        self.nachnameLineEdit = QLineEdit()
        self.geburtstagLineEdit = QDateEdit()
        self.geburtstagLineEdit.setDisplayFormat("dd/MM/yyyy")
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countriesLineEdit = QComboBox()

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Nachname:", self.nachnameLineEdit)
        layout.addRow("Geburtstag:", self.geburtstagLineEdit)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("PLZ:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.countriesLineEdit)
        self.countriesLineEdit.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Menü erstellen:
        menubar = self.menuBar()

        filemenu = menubar.addMenu("File")
        
        save = QAction("Save", self)
        save.triggered.connect(self.daten_speichern)      
        quit = QAction("Quit", self)
        quit.triggered.connect(QApplication.quit)

        filemenu.addAction(save)
        filemenu.addAction(quit)

        viewmenu = menubar.addMenu("View")
        
        karte = QAction("Karte", self)
        karte.triggered.connect(self.karte_anzeigen)       
        load = QAction("Laden", self)
        load.triggered.connect(self.daten_laden)

        viewmenu.addAction(karte)
        viewmenu.addAction(load)

        # Button im Fenster:
        button = QPushButton("Save")
        button.clicked.connect(self.daten_speichern)

        load_btn = QPushButton("Load")
        load_btn.clicked.connect(self.daten_laden)
        
        show_map_btn = QPushButton("Auf Karte zeigen")
        show_map_btn.clicked.connect(self.karte_anzeigen)

        layout.addWidget(button)
        layout.addWidget(load_btn)
        layout.addWidget(show_map_btn)

        # Zentrales Widget erstellen und layout hinzufügen:
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen:
        self.setCentralWidget(center)

        # Fenster anzeigen:
        self.show()

    # daten_speichern Methode erstellen:
    def daten_speichern(self):
        print("Datei wurde gespeichert") 
        daten = [
            self.vornameLineEdit.text(),
            self.nachnameLineEdit.text(),
            self.geburtstagLineEdit.text(),
            self.adresseLineEdit.text(),
            self.plzLineEdit.text(),
            self.ortLineEdit.text(),
            self.countriesLineEdit.currentText()
        ]

        with open('output.txt', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(daten)
    
    # daten_laden Methode erstellen:
    def daten_laden(self):
        file_name, typ = QFileDialog.getOpenFileName(self, "Datei laden", "", "Textdateien (*.txt)")
        
        if file_name:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                daten = next(reader)  # Nur die erste Zeile lesen
                self.vornameLineEdit.setText(daten[0])
                self.nachnameLineEdit.setText(daten[1])
                dformat = QLocale().dateFormat(format=QLocale.FormatType.ShortFormat)
                self.geburtstagLineEdit.setDate(QDate.fromString(daten[2], dformat))
                self.adresseLineEdit.setText(daten[3])
                self.plzLineEdit.setText(daten[4])
                self.ortLineEdit.setText(daten[5])
                self.countriesLineEdit.setCurrentText(daten[6])
    
    # karte_anzeigen Methode erstellen:
    def karte_anzeigen(self):
        address = f"{self.adresseLineEdit.text()}+{self.plzLineEdit.text()}+{self.ortLineEdit.text()}+{self.countriesLineEdit.currentText()}"
        encoded_address = urllib.parse.quote(address)
        link = f"https://www.google.ch/maps/place/{encoded_address}"
        QDesktopServices.openUrl(QUrl(link))

def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()    
    mainwindow.raise_() 
    sys.exit(app.exec_())        

if __name__ == '__main__':
    main()
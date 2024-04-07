import sys
from PyQt5.QtWidgets import *
import csv

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")
        
        layout = QFormLayout()

        # Widget-Instanzen erstellen und als Instanzvariablen speichern:
        self.vornameLineEdit = QLineEdit()
        self.nachnameLineEdit = QLineEdit()
        self.ageSpinBox = QSpinBox()
        self.adresseLineEdit = QLineEdit()
        self.plzLineEdit = QLineEdit()
        self.ortLineEdit = QLineEdit()
        self.countriesLineEdit = QComboBox()

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        save = QAction("Save", self)
        save.triggered.connect(self.daten_speichern)
        quit = QAction("Quit", self)
        quit.triggered.connect(QApplication.quit)

        filemenu.addAction(save)
        filemenu.addSeparator()
        filemenu.addAction(quit)

        button = QPushButton("Save")
        button.clicked.connect(self.daten_speichern)

        # Layout füllen:
        layout.addRow("Vorname:", self.vornameLineEdit)
        layout.addRow("Nachname:", self.nachnameLineEdit)
        layout.addRow("Age:", self.ageSpinBox)
        layout.addRow("Adresse:", self.adresseLineEdit)
        layout.addRow("PLZ:", self.plzLineEdit)
        layout.addRow("Ort:", self.ortLineEdit)
        layout.addRow("Land:", self.countriesLineEdit)
        layout.addWidget(button)
        self.countriesLineEdit.addItems(["Schweiz", "Deutschland", "Österreich"])

        # Zentrales Widget erstellen und layout hinzufügen
        center = QWidget()
        center.setLayout(layout)

        # Zentrales Widget in diesem Fenster setzen
        self.setCentralWidget(center)

        # Fenster anzeigen
        self.show()

    # daten_speichern Methode erstellen
    def daten_speichern(self):
        print("Datei wurde gespeichert") 
        daten = [
            self.vornameLineEdit.text(),
            self.nachnameLineEdit.text(),
            str(self.ageSpinBox.value()),
            self.adresseLineEdit.text(),
            self.plzLineEdit.text(),
            self.ortLineEdit.text(),
            self.countriesLineEdit.currentText()
        ]

        with open('output.txt', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(daten)

def main():
    app = QApplication(sys.argv)  
    mainwindow = MyWindow()    
    mainwindow.raise_() 
    sys.exit(app.exec_())        

if __name__ == '__main__':
    main()

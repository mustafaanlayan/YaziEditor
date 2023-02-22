from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

fontTitle=QFont("Arial",24)
fontText=QFont("Arial",14)

class Help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hakkımızda")
        self.setGeometry(200,200,450,250)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout(self)
        textTitle=QLabel("Hakkımızda")
        txtHakkimizda=QLabel("Mustafa ANLAYAN")
        textTitle.setFont(fontTitle)
        txtHakkimizda.setFont(fontText)
        vbox.addWidget(textTitle)
        vbox.addWidget(txtHakkimizda)
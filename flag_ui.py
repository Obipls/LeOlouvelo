# #!/usr/bin/env python
# flag_ui.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 16-2-2015


from country import *

class Flag(QtGui.QWidget):
    """Maakt een Flag Widget bestaande uit een window die gecentreerd wordt
    op het scherm. De window bestaat uit een combo box met landnamen en
    een frame met de kleur van de vlag van het land"""

    def __init__(self):
        """Maakt een Flag object aan met Flag als superclass en een dictionary
        (self.cDict) als attribuut waarin het land met bijhorende vlag in is
        opgeslagen."""
        super(Flag,self).__init__()
        self.cDict = countriesDict()
        self.initUI()

    def initUI(self):
        """Maakt een window aan die gecentreerd wordt op het scherm. In
        de window wordt een combo box met landnamen uit country.py
        aangemaakt. Daarnaast wordt een frame aangemaakt waarin de
        kleur van de vlag van het land zal worden weergegeven."""
        self.box=QtGui.QComboBox(self)
        self.box.activated.connect(self.onActivated)

        self.hbox=QtGui.QHBoxLayout()
        self.hbox.addWidget(self.box)
        self.setLayout(self.hbox)

        self.fbox=QtGui.QFrame(self)
        self.fbox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.hbox.addWidget(self.fbox)

        for self.i in readText():
            self.box.addItem(self.i.getName())

        self.resize(400, 100)
        self.center()
        self.setWindowTitle('Countries flag')
        self.show()

    def getDict(self):
        ""'Methode die de dictionary met landnamen en landkleuren teruggeeft."""
        return self.cDict

    def onActivated(self, text):
        """Methode die de juiste kleur bij het juiste land opzoekt in de country
        dictionary(cDict) en deze in de frame (fbox) weergeeft."""
        country = self.box.currentText()
        cDict = self.getDict()
        flag = cDict.get(country, 'default')
        self.fbox.setStyleSheet("QFrame{background-color:%s}"%flag.name())

    def center(self):
        """Methode die de window op het scherm centreert."""
        qr=self.frameGeometry()
        cp=QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

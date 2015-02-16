# #!/usr/bin/env python
# flag_ui.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 16-2-2015

from PyQt4 import QtCore, QtGui
import sys
from country import *

class Flag(QtGui.QWidget):
    def __init__(self):
        super(Flag, self).__init__()
        self.initUI()

    def initUI(self):

        self.box = QtGui.QComboBox(self)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.box)
        self.setLayout(hbox)

        for i in readText():
            self.box.addItem(i.getName())

        self.resize(400, 100)
        self.center()
        self.setWindowTitle('Countries flag')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

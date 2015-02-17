# #!/usr/bin/env python
# flag_color.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 16-2-2015

import sys
from random import *
from PyQt4 import QtCore, QtGui

class FlagColor(QtGui.QColor):
        """Genereert een willekeurige kleur"""
        
        def __init__(self):
                """Maakt het color object aan door de methode
                color aan te roepen"""
                super(FlagColor,self).__init__()
                self.color()
        
        def color(self):
                """Genereert een willekeurige rgb kleur bestaande uit
                rood, blauw en groen waardes van 0 tot en met 255."""
                self.setRed(randrange(256))
                self.setBlue(randrange(256))
                self.setGreen(randrange(256))


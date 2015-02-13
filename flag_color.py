# #!/usr/bin/env python
# flag_color.py
# Olivier Louwaars s2814714
# 13-2-2015

import sys
from random import *
from PyQt4 import QtCore, QtGui

class FlagColor(QtGui.QColor):
	
	def __init__(self,):
		super(FlagColor,self).__init__()
		self.color()
	
	def color(self):
		self.setRed(randrange(10))
		self.setBlue(randrange(10))
		self.setGreen(randrange(10))

if __name__ == '__main__':
	app=QtGui.QApplication(sys.argv)
	sys.exit(app.exec_())

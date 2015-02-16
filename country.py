# #!/usr/bin/env python
# country.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 12-2-2015

from flag_color import *
from flag_ui import *

class Country:
        
        def __init__(self,country):
                self.country=country
                self.flag = FlagColor()

        def getName(self):
                return self.country

        def getFlag(self):
                return self.flag

        def __str__(self):
                return "Hello from {}".format(self.country)

def readText():
        countryList=[]
        infile=open("countries_list.txt")
        for line in infile:
                country=line.strip()
                countryList.append(Country(country))
        return countryList

def countriesDict():
        cDict = {}
        for c in readText():
                cDict[c.getName()] = c.getFlag()
        return cDict


if __name__ == "__main__":
        app=QtGui.QApplication(sys.argv)
        ex=Flag()
        sys.exit(app.exec_())


# #!/usr/bin/env python
# country.py
# Olivier Louwaars s2814714 en Leonardo Losno Velozo s1668501
# 16-02-2015

from flag_color import *
from flag_ui import *

class Country:
        """Maakt een Country object aan met als attributen
        de naam van een land (self.country) en
        de vlagkleur van dat land (self.flag)."""

        def __init__(self,country):
                """Maakt een Country object aan bestaande uit
                twee atributen: self.country wordt uit een
                bestand met landnamen gehaald; self.flag wordt
                geïmporteerd uit de Class FlagColor die een
                willekeurige kleur genereert."""
                self.country=country
                self.flag = FlagColor()

        def getName(self):
                """Methode die de naam van het object terug geeft"""
                return self.country

        def getFlag(self):
                """Methode die de kleur van het object terug geeft"""
                return self.flag

        def __str__(self):
                """Methode die bepaalt hoe het object reageert op een print statement"""
                return "Hello from {}".format(self.country)

def readText():
        """Functie die uit het bestand countries_list.txt de landnamen haalt, de newlines verwijdert
        en deze als object in de countryList toevoegt"""
        countryList=[]
        infile=open("countries_list.txt")
        for line in infile:
                country=line.strip()
                countryList.append(Country(country))
        return countryList

def countriesDict():
        """Functie die een dictionary(cDict) aanmaakt met de landnaam
        (self.country) van het Country object als key en de vlagkleur
        (self.flag) als value.""" 
        cDict={}
        for c in readText():
                cDict[c.getName()]=c.getFlag()
        return cDict


if __name__=="__main__":
        app=QtGui.QApplication(sys.argv)
        ex=Flag()
        sys.exit(app.exec_())


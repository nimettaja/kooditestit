# -*- coding: latin-1 -*-
import getpass 
vip = ["Teemu", "Rasmus"]
nimi = raw_input("Nimesi pls (vain etunimi ja oikeinkirioitus): ")
if nimi in vip:
	print "ur in"
else: 
	print "fuk u"

aprint "Tervetuloa!"

tunnus = raw_input("Tunnus: ")
salasana = getpass.getpass("Salasana: ")
if tunnus == "aetis" and salasana == "123":
    print "Welcome, Neo."
else:
	print "Try again, skrub..."

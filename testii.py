# -*- coding: latin-1 -*-
import getpass 


vip = ["Teemu", "Rasmus"]
nimi = input("Nimesi pls (vain etunimi ja oikeinkirioitus): ")

if nimi in vip:
	print("ur in")
else: 
	print("fuk u")
	
print("Tervetuloa!")

tunnus = input("Tunnus: ")
salasana = getpass.getpass("Salasana: ")
if tunnus == "aetis" and salasana == "123":
	print "Welcome, Neo."
else:
	print "Try again, skrub..."

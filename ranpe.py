def main():
	print "Nimesi:"
	name = raw_input()
	print "Moi,", name
	print "Plus-laskin"
	a = input("Valitse numero:")
	b = input("Sano toinen numero:")
	c = a + b
	print a, "plus", b, "on yhtasuuri kuin ", c
	print "Mika on lempivarisi?"
	name = raw_input()
	print "Jaa, lempivarisi on siis", name
	print "Rasmuksen eka python ohjelma loppu tahan"
	print "(c) RasmusK"
	return 0

if __name__ == '__main__':
	main()

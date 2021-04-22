# zadej cislo a prekonvertuj ho binarnina 32bit binarni cislo

cislo = int(input("Zadej cislo: "))

nove_cislo = "{0:>032b}".format(cislo)
print(nove_cislo)
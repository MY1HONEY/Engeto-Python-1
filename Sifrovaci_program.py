# Cesarova sifra
print("*** SIFROVACI PROGRAM ***")

mod = True

while mod:

    operace = input("""
+----------------+
|Seznam operaci: |
+----------------+
|[s]ifrovat      |
|[d]esifrovat    |
|[k]onec         |
+----------------+
 """)

    if operace == "s":
        sifra = input("Zadej text, ktery ma byt zasifrovan: ")
        klic = int(input("Zadejte klic sifrovani: "))
        
        vysledek = ""
        for i in sifra:
            kod = ord(i)
            kod = kod + klic
            vysledek = vysledek + chr(kod)
        print("Sifra: ",vysledek)

    elif operace == "d":
        sifra = input("Zadej text, ktery ma byt desifrovan: ")
        klic = int(input("Zadejte klic sifrovani: "))
        
        vysledek = ""
        for i in sifra:
            kod = ord(i)
            kod = kod - klic
            vysledek = vysledek + chr(kod)
        print("Sifra: ",vysledek)

    elif operace == "k":
        print("Program byl ukoncen")
        mod = False

    else:
        print("Musis zadat s, d nebo k.")

data = {'uzivatel1': 'heslo1', 'Marek': '1234', 'Danko': 'qwert'}

jmeno = input("Zadejte Vase jmeno: ")
heslo = input("Zadejte Vase heslo: ")

if data.get(jmeno) == heslo:
    print("Uzivatelske jmeno:", jmeno)
    print("Heslo:", heslo)
    print("Pristup udelen.")
else:
    print("Uzivatelske jmeno:", jmeno)
    print("Heslo:", heslo)
    print("Zadal jse spatne jmeno nebo heslo.")





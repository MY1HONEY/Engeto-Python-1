print('Vitejte v programu "Kalkulacka".')
hodnota_A = float(input("Zadejte prvni cislo: "))
hodnota_B = float(input("Zadejte druhe cislo: "))

mod = True

while mod:
    choice = str(input('''
------------------------
Sčítání:    "sci",
Odčítání:   "odc",
Násobení:   "nas",
Dělení:     "del",
Ukonči:     "off",
----------------------
Vyber si operaci: '''))
    if choice == "sci":
        vysledek = hodnota_A + hodnota_B
        print(hodnota_A,"+",hodnota_B,"=",vysledek)
    elif choice == "odc":
        vysledek = hodnota_A - hodnota_B
        print(hodnota_A,"-",hodnota_B,"=",vysledek)
    elif choice == "nas":
        vysledek = hodnota_A * hodnota_B
        print(hodnota_A,"*",hodnota_B,"=",vysledek)
    elif choice == "del":
        vysledek = hodnota_A / hodnota_B
        print(hodnota_A,"/",hodnota_B,"=",vysledek)
    elif choice == "off":
        print("Program byl ukoncen.")
        mod = False
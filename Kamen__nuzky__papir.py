import random

moznost = ["kamen","nuzky","papir"]

hrac = input("Zadej kamen/nuzky/papir: ")
pocitac =  random.choice(moznost)

print("Hrac zvolil", hrac," a pocitac", pocitac)


if hrac != 'kamen' and hrac != 'nuzky' and hrac != 'papir':
    print("Neplatna volba")
else:
    if hrac == 'kamen' and pocitac == 'nuzky':
        print("Vyhral jsi")
    elif hrac == 'nuzky' and pocitac == 'papir':
        print("Vyhral jsi")
    elif hrac == 'papir' and pocitac == 'kamen':
        print("Vyhral jsi")
    elif hrac == pocitac:
        print("Nerozhodne")
    else:
        print("Prohral jsi")





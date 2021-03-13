#Tvým úkolem bude napsat skript, který nechá uživatele hádat slovo z tříčlenného listu ovoce. Uživatel má 2 pokusy na odpověď, jinak prohrál.

import random

ovoce = ['jablko', 'banan', 'hruska']

pokus = 0
while pokus < 2:
    slovo_hrac = input("Zadej ovoce 'jablko', 'banan' nebo 'hruska': ")
    slovo_pocitac = random.choice(ovoce)

    if slovo_hrac != slovo_pocitac:
        print("Hrac vybral",slovo_hrac,"pocitac vybral",slovo_pocitac,".")    
        pokus = pokus + 1
        print("Pocet pokusu celkem:",pokus,".")
        if pokus == 2:
            print("Bylo zadano maximum pokusu, prohral jsi.")
    else:
        print("Hrac vybral",slovo_hrac,"pocitac vybral",slovo_pocitac,".")
        print("Vyhral jsi.")
        break



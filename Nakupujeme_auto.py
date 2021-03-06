# Cenik
mercedes    = 150000
rolls_royce = '400000'
vybava = 50000

rolls_royce = int(rolls_royce)

#Cenu za dva Mercedesy
two_mercedes = mercedes * 2

#cenu za Mercedes a Rolls-Royce
mercedes_rolls = mercedes + rolls_royce

#cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich),
two_rolls_extrpacket = 2 * rolls_royce + 2 * vybava

#cenu za Mercedes s příplatkovou výbavou.
mercedes_extrpacket = mercedes + vybava

#následně vytvoř proměnnou, která si od uživatele vyžádá libovolnou slevu na mercedes a do další proměnné ulož slevu na mercedes.
discount = int(input("Vloz libovolnou slevu na mercedes: "))

#Nakonec by měl program všechno přehledně vypsat. Pusť se do toho.
print("Cena za dva Mercedesy je", two_mercedes,".")
print("Cena za Mercedes a Rolls Royce je",mercedes_rolls,".")
print("Cena za dva Rolls Royce s priplatkovou vybavou je",two_rolls_extrpacket,".")
print("Cena za Mercedes s priplatkovou vybavou je",mercedes_extrpacket,".")
print("Uzivatelem vytvorena sleva je",discount,".")
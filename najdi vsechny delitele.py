cislo = int(input("Zadej cislo: "))

delitel = ()

for i in range (1, cislo + 1):
    if cislo % i == 0:
        delitel = delitel + (i,)
    
print("cislo {} delitelne {}".format(cislo, delitel))

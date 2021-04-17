import random

a = "+-------+"
b = "| {} {} {} |"

nahodne_cislo = random.randint(1,6)

#1
if nahodne_cislo == 1:
    print(a)
    print((b).format(" "," "," "))
    print((b).format(" ","o"," "))
    print((b).format(" "," "," "))
    print(a)

#2
elif nahodne_cislo == 2:
    print(a)
    print((b).format("o"," "," "))
    print((b).format(" "," "," "))
    print((b).format(" "," ","o"))
    print(a)

#3
elif nahodne_cislo == 3:
    print(a)
    print((b).format("o"," "," "))
    print((b).format(" ","o"," "))
    print((b).format(" "," ","o"))
    print(a)

#4
elif nahodne_cislo == 4:
    print(a)
    print((b).format("o"," ","o"))
    print((b).format(" "," "," "))
    print((b).format("o"," ","o"))
    print(a)

#5
elif nahodne_cislo == 5:
    print(a)
    print((b).format("o"," ","o"))
    print((b).format(" ","o"," "))
    print((b).format("o"," ","o"))
    print(a)

#6
else:
    print(a)
    print((b).format("o"," ","o"))
    print((b).format("o"," ","o"))
    print((b).format("o"," ","o"))
    print(a)

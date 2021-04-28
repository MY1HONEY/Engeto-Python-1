
x = 8

#1
def spolecni_delitele(x):
    delitel = []
    for i in range (1, x + 1):
        if x % i == 0:          
            delitel.append(i)
    return delitel
print(spolecni_delitele(x))

#2
def perfektni_cisla(x):
    soucet = sum(spolecni_delitele(x)) - x
    if soucet == x:
        soucet = True
    elif soucet != x:
        soucet = False
    return soucet
print(perfektni_cisla(x))













            

        

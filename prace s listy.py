#1
cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
suda_cisla = []

for i in cisla:
    if i%2 == 0:
        suda_cisla.append(i)
print(suda_cisla)

#2
cisla = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
nova_cisla = []

for i in cisla:
    if i > 0:
        i = round(i)
        nova_cisla.append(i)
print(nova_cisla)

#3
veta = "the quick brown fox jumps over the lazy dog"
slova = veta.split()
seznam_delka = []

for i in slova:
    if i != "the":
        delka = len(i)
        seznam_delka.append(delka)
print(seznam_delka)


   


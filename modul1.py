#Úloha 1

cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nove_cisla = [ x for x in cisla if x%2==0]
print(nove_cisla)

#Úloha 2

cisla_1 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
a = [ round(b) for b in cisla_1 if b > 0 ]
print(a)

#Úloha 3

veta = "the quick brown fox jumps over the lazy dog"
slova = veta.split()
slova_delka = [ len(i) for i in slova if i != "the" ]
print(slova_delka)

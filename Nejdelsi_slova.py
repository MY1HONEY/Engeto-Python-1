#Napiš program, který z listu slova vybere nejdelší slovo a vytiskne do terminálu tuple s tímto nejdelším slovem a jeho délkou.

#Použij prosím tento list:

slova = [
    'Python', 'is', 'a', 'widely', 'used',
    'high-level', 'programming', 'language',
    'for', 'general-purpose', 'programming,',
    'created', 'by', 'Guido', 'van', 'Rossum',
    'and', 'first', 'released', 'in', '1991.'
]



# 1.
nejdelsi_slovo = ('', 0) #prvni prvek je slovo, druhy prvek jeho delka

while slova:
    # 2.
    slovo = slova.pop(0) #vybereme pocatecni slovo z listu "slova"
    # 3.
    if len(slovo) > nejdelsi_slovo[1]: #porovnavame delku vybraneho slova z listu proti slovu, ktere je ulozene v "nejdelsi_slovo", index [1] znamena, ze bere jeho delku, ktera je ulozena na teto pozici
        # 4.
        nejdelsi_slovo = slovo, len(slovo) #pokud je nove slovo delsi nez to predchazejici, prepise jim promenou "nejdelsi_slovo", cyklus je ukoncen a dochazi k porovnanvani noveho slova, tak dlouho dokud nedojde k porovnani vsech slov v listi "slova"
# 5.
print(nejdelsi_slovo)

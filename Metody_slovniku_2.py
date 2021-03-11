# slovniky
slovnik01 = {'jmeno': 'David', 'prijmeni': 'Novak', 'vek': 33}
slovnik02 = {'pismena': ['a', 'b', 'c', 'd'], 'cisla': [1,2,3,4,5]}
slovnik03 = {'zamestnanci': {'id01': 'Marek', 'id02': 'Matous', 'id03': 'Anna'}, 'adresy': {'id01': 'Brno', 'id02': 'Praha', 'id03': 'Praha'}}

#získej pomocí vhodné metody kolekci dvojic klíčů a hodnot ze slovníku slovnik01 a ulož je do proměnné klice_hodnoty,
klice_hodnoty = slovnik01.items()
print(klice_hodnoty)

#získej pomocí vhodné metody jenom kolekci klíčů slovníku slovnik02 a ulož je do proměnné klice,
klice = slovnik02.keys()
print(klice)

#získej pomocí vhodné metody ze slovníku slovnik03 jenom hodnoty a ulož jej do proměnné hodnoty,
hodnoty = slovnik03.values()
print(hodnoty)

#zkus získat pomocí vhodné metody ze slovníku slovnik03 hodnoty z vnitřního slovníku 'zamestnanci' a ulož jej do proměnné vyzva.
vyzva = slovnik03["zamestnanci"].values()
print(vyzva)



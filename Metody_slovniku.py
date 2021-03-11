#přiraď do proměnných muj_slovnik a novy_slovnik prázdné slovníky,

muj_slovnik = {}
novy_slovnik = {}

#do proměnné muj_slovnik vlož tyto klíče: 'jméno', 'přijmení'. Pro klíče vytvoř jejich libovolné hodnoty,

jmeno = {"jmeno":"Tomas"}
prijmeni = {"prijmeni":"Novak"}

muj_slovnik.update(jmeno)
muj_slovnik.update(prijmeni)


#vytvoř pomocí vhodné metody z tuple 'muj_tuple' slovník a ten ulož do slovníku novy_slovnik,

muj_tuple = 'věk', 'email'

novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

#muj_slovnik doplň o novy_slovnik pomocí metody update,

muj_slovnik.update(novy_slovnik)

#přiraď hodnoty klíčům 'věk' a 'email'. Email by mněl obsahovat zavináč '@'.

vek = {"vek":"25"}
email = {"email":"Novak@email.com"}

muj_slovnik.update(vek)
muj_slovnik.update(email)

print("Můj slovník: " + str(muj_slovnik))
print("Nový slovník: " + str(novy_slovnik))
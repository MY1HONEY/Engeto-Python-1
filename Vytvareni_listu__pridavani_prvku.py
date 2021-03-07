# Tvým úkolem je napsat kód, který:

# Proměnné kandidati přiřadí prázdný list.
kandidati = []

# Vytiskne obsah proměnné kandidati za větu 'Kandidáti na začátku: '.
print("Kandidati na zacatku",kandidati)

# Do proměnné zamestnanci přiřadí list, který bude obsahovat stringy: 'František', 'Anna', 'Jakub', 'Klára'.
zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']

# Vytiskne obsah zamestnanci za větu 'Zaměstnanci na začátku: '.
print("Zamestnanci na zacatku",zamestnanci)

# Do prázdného listu kandidáti přidá jména 'Bruno' a 'Anežka'.
kandidati.append("Bruno")
kandidati.append("Anezka")

# Vytiskne obsah listu kandidati za string 'Nová jména přidána do kandidati: '.
print("Nova jmena pridana do kandidati",kandidati)

# Vloží jméno 'Bruno', uložené v listu kandidati, do listu zamestnanci na pozici index 1.
zamestnanci.insert(1, "Bruno")

# Vytiskne obsah proměnné zamestnanci za string: 'Nová jména vložena do zamestnanci: '.
print("Nova jmena vlozena za zamestnanci:",zamestnanci)

# Odstraní prvek 'Bruno' z listu kandidati.
kandidati.remove("Bruno")

# Vytiskne obsah proměnné kandidati za string: 'Bruno odstraněn z kandidati: '.
print("Bruno odstranen z kandidati:",kandidati)

# Zopakovat jméno 'Anežka' uvnitř listu kandidati.
kandidati = ["Anezka"]* 2

# Vytisknout obsah listu kandidati za string: 'Opakování prvku Anežka v kandidati:'.
print("Opakovani prvku Anezka v kandidati:",kandidati)

# Spoj list zamestnanci s listem kandidati do nového listu, který zachová název zamestnanci.
zamestnanci = zamestnanci + kandidati

# Vytiskni obsah nového listu zamestnanci za string: 'Spojeni kandidati a zamestnanci: '.
print("Spojeni kadidati a zamestnanci:",zamestnanci)

# Vytisknout jméno na indexu 2 za string: 'Na indexu 2 je: '.
print("Na indexu 2 je:",zamestnanci[2])

# Vytisknout jméno na posledním indexu za string: 'Na <posledni_index> indexu je: '.
print("Na poslednim indexu je:",zamestnanci[-1])

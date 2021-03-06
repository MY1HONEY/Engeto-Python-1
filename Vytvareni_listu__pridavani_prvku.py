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
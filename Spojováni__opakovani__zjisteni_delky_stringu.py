#Vytvoř skript, který:

# Vyžádá jméno od uživatele a uloží jej do proměnné jmeno.
jmeno = input("Zadejte Vase jmeno: ")

# Vytiskne proměnnou jmeno.
print(jmeno)

# Vyžádá přijmení od uživatele a uloží jej do proměnné prijmeni.
prijmeni = input("Zadejte Vase prijmeni: ")

# Vytiskne proměnnou prijmeni.
print(prijmeni)

# Vytvoří proměnnou cele_jmeno, do které uložíš spojení proměnné jmeno a prijmeni oddělené mezerou.
cele_jmeno = jmeno + " " + prijmeni

# Vytiskne proměnnou delka_jmena, která bude obsahovat hodnotu délky celého jména.
delka_jmena = len(cele_jmeno)
print(delka_jmena)

# Vytiskne proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek. K tomu použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje string uložen v proměnné cele_jmeno
print(delka_jmena * "=")
print(cele_jmeno)
print(delka_jmena * "=")
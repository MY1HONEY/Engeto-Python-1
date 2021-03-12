# Zadany string
muj_string = 'Abc@abc.cz a Matous@1234.cz jsou naše emailové adresy'

#do proměnné rozdeleny_string ulož muj_string jako list rozdělený podle mezer.

rozdeleny_string = muj_string.split()
print(rozdeleny_string)

#do proměnné emaily přidej pouze emailové adresy pomocí jejich indexu v proměnné rozdeleny_string.
email01 = rozdeleny_string[0]
email02 = rozdeleny_string[2]
emaily = email01 + " " + email02 
print(emaily)

#získej pouze domény (text za znakem '@') z emailů v listu emaily. První doménu ulož do proměnné domena01 a druhou do domena02.
domena01 = email01.split("@")
domena01 = domena01[1]
domena02 = email02.split("@")
domena02 = domena02[1]
print(domena01)
print(domena02)

#rozděl stringy v promměnných domena01 a domena02 podle znaku '.' a ulož pouze první prvek (na indexu 0) do stejné proměnné.
domena01 = domena01.split(".")
domena01 = domena01[0]
domena02 = domena02.split(".")
domena02 = domena02[0]
domena = domena01 + " " + domena02
print(domena)

#ověř pomocí podmínky if, zda proměnná domena01 neobsahuje žádná čísla.

bez_cisel = ""
if domena01.isalpha() == True:
    bez_cisel = bez_cisel.join(domena01) #přiřaď kód pod příkaz if, který spojí s prázdným stringem bez_cisel pouze tu doménu, která neobsahuje číslice.
    print("domena01 neobsahuje zadna cisla")
    print("domena", domena01,"byla pridana") #pod příkaz if funkci print(), která vypíše následující: 'Doména', <doména>, 'byla přidána.'.
else:
    print("domena01 obsahuje cisla")

if domena02.isalpha() == True:
    bez_cisel = bez_cisel.join(domena02) #přiřaď kód pod příkaz if, který spojí s prázdným stringem bez_cisel pouze tu doménu, která neobsahuje číslice.
    print("domena02 neobsahuje zadna cisla")
    print("domena", domena02,"byla pridana") #pod příkaz if funkci print(), která vypíše následující: 'Doména', <doména>, 'byla přidána.'.
else:
    print("domena02 obsahuje cisla")
print(bez_cisel)




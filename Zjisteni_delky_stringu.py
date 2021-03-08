#Vytvoř skript, který:

#přijme jakékoli slovo od uživatele a uloží ho do proměnné slovo
slovo = input("Zadej jakekoliv slovo: ")

#zjistí a vytiskne délku zadaného slova

delka = len(slovo)

if delka > 4:
    print(slovo,"obsahuje",delka,"znaku")
elif delka < 5 and delka > 1:
    print(slovo,"obsahuje",delka,"znaky")
elif delka == 1:
    print(slovo,"obsahuje",delka,"znak")
else:
    print("nebylo zadano zadne slovo")


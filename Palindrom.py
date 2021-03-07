# Palindrom

slovo = input("Zadejte slovo: ")

prevracene_slovo = slovo[::-1]

if slovo == prevracene_slovo:
    print("Slovo",slovo,"je palindrom.")
else:
    print("Slovo",slovo,"neni palindrom.")



sirka = int(input("Zarovnejte tabulku na: "))

ramecek = ("+" + "-" * ((sirka * 4) + 3) + "+")
hlavicka = ("|{:^{width}}|{:^{width}}|{:^{width}}|{:^{width}}|".format("dec","bin","oct","hex", width=sirka))

print(ramecek)
print(hlavicka)
print(ramecek)

for i in range (0, 16):
    print("|{0:>{sirka}d}|{0:>#{sirka}b}|{0:>#{sirka}o}|{0:>#{sirka}x}|".format(i, sirka = sirka))

print(ramecek)
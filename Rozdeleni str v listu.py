seznam = ["Jan Novak","jana Novakova","Lukas kralik"]

chybny_seznam = []
opraveny_seznam = []

# vypise chybna jmena
for i in seznam:
    if i.split()[0].istitle() == False or i.split()[1].istitle() == False:
        chybny_seznam.append(i)
print(chybny_seznam)

# opravi chybna jmena
for i in seznam:
    seznam = i.title()
    opraveny_seznam.append(seznam)
print(opraveny_seznam)
    
    


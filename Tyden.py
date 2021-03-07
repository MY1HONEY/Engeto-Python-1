tyden = ["pondeli", "utery", "streda", "ctvrtek", "patek", "sobota", "nedele"]

den_cislo = int(input("Vyberte den v tydnu, pomoci cisla (1-pondeli): "))
den_pismeno = input("Vyberte pocatecni pismeno, kterym zacina tento den: ")

if (tyden[den_cislo-1][0]) == den_pismeno:
    print("True")
else:
    print("False")
    
  



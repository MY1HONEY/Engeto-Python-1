import random

print("""
  /\/\   __ _ ___| |_ ___ _ __ /\/\ (_)_ __   __| |
 /    \ / _` / __| __/ _ \ '__/    \| | '_ \ / _` |
/ /\/\ \ (_| \__ \ ||  __/ | / /\/\ \ | | | | (_| |
\/    \/\__,_|___/\__\___|_| \/    \/_|_| |_|\__,_|
""")

jmeno = input("Zadej jmeno hrace: ")
print("")

if jmeno == "":
    print("    Vitej ve hre MasterMind, zde jsou pravidla:")
else:
    print("    Vitej", jmeno,"ve hre MasterMind, zde jsou pravidla")

print("""
    Pocitac si mysli vzdy jedno cislo od 1 do 10. 
    Tvym ukolem je toto cislo uhadnout. 
    Hadej kolikrat chces.
    Pokud budes chtit ukoncit hru napis "konec" a vypise se tve skore.
""")

pocitac = random.randint(1, 10)

mod = True
i = 0 # pokusy
s = 0 # spravne pokusy
n = 0 # nespravne pokusy

while mod:
    hrac = input("Tvuj pokus, hadej: ")
    i = i + 1 
    if hrac == "konec":
        print("Konec hry.")
        print("+------------------------------+")
        print("|Celkem pocet pokusu:       ",i-1,"|")
        print("|Pocet nespravnych pokusu:  ",n,"|")
        print("|Pocet spravnych pokusu:    ",s,"|")
        print("+------------------------------+")
        mod = False
    elif int(hrac) != pocitac:
        print("Hadej znovu.")
        print("Pocet pokusu", i)   
        n = n + 1
        if int(hrac) > 10 or int(hrac) < 1:
            print("Zadavej pouze cisla od 1 do 10!")
    elif int(hrac) == pocitac:
        print("Uhadl jsi!")
        print("Pocet pokusu", i)
        pocitac = random.randint(1, 10)
        s = s + 1
    


  
    
    
    
    
    
    
    
     
    
    
    
    
        
        
            



            
        
        

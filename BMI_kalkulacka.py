# BMI kalukacka

#Hodnota	Význam
#do 18,5	Podvýživa
#18,5 – 25	Zdravá váha
#25 – 30	Mírná nadváha
#30 – 40	Obezita
#40 a více	Těžká obezita

vyska = float(input("Zadejte Vasi vysku v metrech: "))
vaha = float(input("Zadejte Vasi hmotnost v kg:"))

# Vypocet BMI
bmi = vaha/(vyska**2)

# Telo programu
if bmi < 18.5:
    print("Tve BMI je",bmi,", coz spada do kategorie podvyziva.")
elif bmi < 25:
    print("Tve BMI je",bmi,", coz spada do kategorie zdrava vaha.")
elif bmi < 30:
    print("Tve BMI je",bmi,", coz spada do kategorie mirna nadvaha.")
elif bmi < 40:
    print("Tve BMI je",bmi,", coz spada do kategorie obezita.")
else:
    print("Tve BMI je",bmi,", coz spada do kategorie tezka obezita.")

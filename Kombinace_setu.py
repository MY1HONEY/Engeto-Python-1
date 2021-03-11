str1 = 'New York'
str2 = 'Yorkshire'
#ulož do proměnné spolecne prvky, které mají str1 a sa metody stringu str2 společné,

spolecne = set(str1) & set(str2)
print(spolecne)

#ulož do proměnné unikatni prvky, které jsou unikátní pro str1,

unikatni = set(str1) - set(str2)
print(unikatni)

#ulož do proměnné nesdilene prvky, které str1 a str2 nesdílí. Jinak řečeno, prvky, které se nachází v str1, str2, ale ne v obou,

nesdilene = set(str1) ^ set(str2)
print(nesdilene)

#ulož do proměnné vsechny prvky, které str1 a str2 sdílí i nesdílí - všechny prvky,

vsechny = set(str1) | set(str2)
print(vsechny)



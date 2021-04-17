a = "+-------+"
b = "| {} {} {} |"

#1

print(a)
print((b).format(" "," "," "))
print((b).format(" ","o"," "))
print((b).format(" "," "," "))
print(a)

#2

print(a)
print((b).format("o"," "," "))
print((b).format(" "," "," "))
print((b).format(" "," ","o"))
print(a)

#3

print(a)
print((b).format("o"," "," "))
print((b).format(" ","o"," "))
print((b).format(" "," ","o"))
print(a)
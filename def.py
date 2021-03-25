x = int(input("Insert number: "))
y = int(input("Insert number: "))


def first_num(x,y):
    num = []
    for a in range(x,y):
        num.append(a)
    return num[0]

def last_num(x,y):
    num = []
    for b in range(x,y):
        num.append(b)
    return num[-1]

def count_num(x,y):
    num = []
    for c in range(x,y):
        num.append(c)
    return sum(num)

result = first_num(x,y), last_num(x,y), count_num(x,y)
print(result)






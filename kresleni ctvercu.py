import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480, bg="white")
canvas.pack()

def barva(vzd):
    x = int((vzd/400)*255)
    return "#{:02x}{:02x}{:02x}".format(x,x,x)

def vzdalenost(x, y):
    return ((x-320)**2 + (y-240)**2)**0.5

def kreslit_ctverce(x, y, velikost, barva):
    souradnice = x-velikost/2, y-velikost/2, x+velikost/2, y+velikost/2
    canvas.create_rectangle(souradnice, fill=barva)

for x in range(1000):
    x = random.randrange(640)
    y = random.randrange(480)
    vzd = vzdalenost(x, y)
    b = barva(vzd)
    kreslit_ctverce(x, y, vzd/6, b)

canvas.mainloop()

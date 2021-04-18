import random
import tkinter

canvas = tkinter.Canvas(width = 640, height = 480)
canvas.pack()

for i in range(1000):
    x = random.randrange(640)
    y = random.randrange(480)

    if x < 160:
        barva = "red"
    elif x <= 320 and x >= 160:
        barva = "yellow"
    elif x <= 480 and x >= 320:
        barva = "purple"
    else:
        barva = "blue"

    canvas.create_oval(x,y,x+10,y+10, fill = barva)
    
canvas.mainloop()
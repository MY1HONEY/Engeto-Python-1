# obrazec kruhy

import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


x, y = 0, 0
size = int(input("Zadej velikost kruhu: "))

canvas.create_oval(x,         y,           x+size,           y+size)
canvas.create_oval(x,         y+size/2,    x+size,           y+size+(size/2))
canvas.create_oval(x,         y+size,      x+size,           y+(size*2))

canvas.create_oval(x+size/2,  y,           x+size+(size/2),  y+size)
canvas.create_oval(x+size/2,  y+(size/2),  x+size+(size/2),  y+size+(size/2))
canvas.create_oval(x+size/2,  y+size,      x+size+(size/2),  y+(size*2))

canvas.create_oval(x+size,    y,           x+(size*2),       y+size)
canvas.create_oval(x+size,    y+(size/2),  x+(size*2),       y+size+(size/2))
canvas.create_oval(x+size,    y+size,      x+(size*2),       y+(size*2))

canvas.mainloop()

# olympijske kruhy

import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadej polomer kruhu: "))
x = int(input("Zadej pocatecni x souradnici: "))
y = int(input("Zadej pocatecni y souradnici: "))
offset = r * 0.2

canvas.create_oval(x,                          y,   x+r*2,                     y+r*2,outline ="#00f", width=5)
canvas.create_oval(x+(2*r)+offset,             y,   x+(r*4)+offset,            y+r*2,outline ="#000", width=5)
canvas.create_oval(x+(4*r)+offset*2,           y,   x+(r*6)+offset*2,          y+r*2,outline ="#f00", width=5)

canvas.create_oval(x+(2*r+offset/2)/2,         y+r, x+(6*r+offset/2)/2,        y+r*3,outline ="#ff0", width=5)
canvas.create_oval(x+offset*2+(3*r+offset/2),  y+r, x+offset*2+(5*r+offset/2), y+r*3,outline ="#0f0", width=5)

canvas.mainloop()


import tkinter
import random

number = random.randint(1,6)

print("Na kostce padlo cislo {}.".format(number))
print("Vykresluji kostku...")

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

# Souradnice stredu kostky.
x, y = canvas_width / 2, canvas_height / 2 

# Definovani promennych - velikost kostky.
# Pouzijeme polygon pro vykresleni obrysu kostky, "radius" použijeme na vypocitani zeseknuti hrany.
#
#    p2___p3
# p1/       \p4
#   |       |
#   |       |
# p8\_______/p5
#   p7    p6
#

size = 300 
radius = size*0.03
unit = size / 5

p1 = x - size / 2,          y-size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,          y-size / 2 + radius
p5 = x + size / 2,          y+size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,          y+size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8, outline="black", fill="gray", width=3)



# Souradnice tecek
#
#        a a a
#        1 2 3
#      +-------+
#   b1 | 1   2 |
#   b2 | 3 4 5 |
#   b3 | 6   7 |
#      +-------+

a1 = x - 1.5*unit
a2 = x
a3 = x + 1.5*unit

b1 = y - 1.5*unit
b2 = y
b3 = y + 1.5*unit

x1, y1 = a1, b1
x2, y2 = a3, b1
x3, y3 = a1, b2
x4, y4 = a2, b2
x5, y5 = a3, b2
x6, y6 = a1, b3
x7, y7 = a3, b3

if number == 1:
    canvas.create_oval(x4-unit/2, y4-unit/2, x4+unit/2, y4+unit/2, fill="white")
elif number == 2:
    canvas.create_oval(x1-unit/2, y1-unit/2, x1+unit/2, y1+unit/2, fill="white")
    canvas.create_oval(x7-unit/2, y7-unit/2, x7+unit/2, y7+unit/2, fill="white")
elif number == 3:
    canvas.create_oval(x1-unit/2, y1-unit/2, x1+unit/2, y1+unit/2, fill="white")
    canvas.create_oval(x7-unit/2, y7-unit/2, x7+unit/2, y7+unit/2, fill="white")
    canvas.create_oval(x4-unit/2, y4-unit/2, x4+unit/2, y4+unit/2, fill="white")
elif number == 4:
    canvas.create_oval(x1-unit/2, y1-unit/2, x1+unit/2, y1+unit/2, fill="white")
    canvas.create_oval(x2-unit/2, y2-unit/2, x2+unit/2, y2+unit/2, fill="white")
    canvas.create_oval(x6-unit/2, y6-unit/2, x6+unit/2, y6+unit/2, fill="white")
    canvas.create_oval(x7-unit/2, y7-unit/2, x7+unit/2, y7+unit/2, fill="white")
elif number == 5:
    canvas.create_oval(x1-unit/2, y1-unit/2, x1+unit/2, y1+unit/2, fill="white")
    canvas.create_oval(x2-unit/2, y2-unit/2, x2+unit/2, y2+unit/2, fill="white")
    canvas.create_oval(x6-unit/2, y6-unit/2, x6+unit/2, y6+unit/2, fill="white")
    canvas.create_oval(x7-unit/2, y7-unit/2, x7+unit/2, y7+unit/2, fill="white")
    canvas.create_oval(x4-unit/2, y4-unit/2, x4+unit/2, y4+unit/2, fill="white")
else:
    canvas.create_oval(x1-unit/2, y1-unit/2, x1+unit/2, y1+unit/2, fill="white")
    canvas.create_oval(x2-unit/2, y2-unit/2, x2+unit/2, y2+unit/2, fill="white")
    canvas.create_oval(x6-unit/2, y6-unit/2, x6+unit/2, y6+unit/2, fill="white")
    canvas.create_oval(x7-unit/2, y7-unit/2, x7+unit/2, y7+unit/2, fill="white")
    canvas.create_oval(x3-unit/2, y3-unit/2, x3+unit/2, y3+unit/2, fill="white")
    canvas.create_oval(x5-unit/2, y5-unit/2, x5+unit/2, y5+unit/2, fill="white")

canvas.mainloop()
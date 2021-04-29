import tkinter as tk

canvas = tk.Tk()
canvas.title("Snehulak")
canvas = tk.Canvas(width=640, height=480)
canvas.configure(bg="#abcae4")
canvas.pack()


x, y = 320, 320 # umisteni snehulaka (stred)
r = 100 # polomer (velikost koule)

# souradnice mrkve
p1 = x, y - 2*r
p2 = x + r/2, y - 2*r
p3 = x, y - 2*r + r*(1/4)

def koule(x,y,r):
    canvas.create_oval(x+r, y+r, x-r, y-r, outline="white", fill="white")

def mrkev (x,y,r):
    canvas.create_polygon(p1, p2, p3, fill="orange")

def oci(x,y,r):
    canvas.create_oval(x-r*(1/10), y-2.1*r, x-r*(1/5), y-2.2*r, fill="black")
    canvas.create_oval(x+r*(1/10), y-2.1*r, x+r*(1/5), y-2.2*r, fill="black")
    
def snehulak(x,y,r):
    koule(x,y,r)
    koule(x,y-r,r*(3/4))
    koule(x,y-2*r,r*(3/5))
    mrkev(x,y,r)
    oci(x,y,r)

snehulak(x,y,r)


canvas.mainloop()


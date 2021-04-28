import tkinter as tk

canvas = tk.Tk()
canvas.title("Snehulak")
canvas = tk.Canvas(width=640, height=480)
canvas.configure(bg="#abcae4")
canvas.pack()


x, y = 320, 320 # umisteni snehulaka (stred)
r = 100 # polomer (velikost koule)

def koule(x,y,r):
    canvas.create_oval(x+r, y+r, x-r, y-r, outline="white", fill="white")

def snehulak(x,y,r):
    koule(x,y,r)
    koule(x,y-r,r*(3/4))
    koule(x,y-2*r,r*(3/5))

snehulak(x,y,r)


canvas.mainloop()


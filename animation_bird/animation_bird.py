import tkinter

main = tkinter.Tk()
bg = tkinter.PhotoImage(file="BG.png")
canvas = tkinter.Canvas(width=bg.width(), height=bg.height())
canvas.pack()

canvas.create_image(bg.width()/2, bg.height()/2, image=bg)

bird = []
for i in range(4):
    img = tkinter.PhotoImage(file="bird/bird_{:02d}.png".format(i))
    bird.append(img)

bird_id = canvas.create_image(bg.width()/2, bg.height()/2)

def animate():
    global sprite_idx
    sprite_idx = (sprite_idx + 1) % 4
    canvas.itemconfig(bird_id, image=bird[sprite_idx])
    canvas.after(50, animate)

sprite_idx = 0

animate()

canvas.mainloop()
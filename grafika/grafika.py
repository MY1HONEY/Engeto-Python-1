import pyglet
import math
 
window = pyglet.window.Window()

def tik(t):
    pokemon01.x = pokemon01.x + t * 20
    pokemon01.y = 20 + 20 * math.sin(pokemon01.x / 5)
    print(t)

pyglet.clock.schedule_interval(tik, 1/30)

def zpracuj_text(text):
    print(text)
    pokemon.x = 150

obrazek = pyglet.image.load('pokemon01.png')#nahraje obrazek ze souboru
pokemon01 = pyglet.sprite.Sprite(obrazek)#definuje pozici obrazku v okne, defaultne v levo dole

def vykresli():#funkce vykresli obrazek
    window.clear()#vycisti okno
    pokemon01.draw()#nakresli obrazek pomoci spritu "pokemon01"

def klik(x, y, tlacitko, mod):
    pokemon01.x = x
    pokemon01.y = y

#zaregistruje funkci "vykresli"
window.push_handlers(
    on_mouse_press=klik,
    on_text=zpracuj_text,
    on_draw=vykresli,#jakekoliv kresleni se musi provadet pomoci funkce "on_draft"
)

obrazek2 = pyglet.image.load('pokemon02.png')

def zmen(t):
    pokemon01.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 1)

def zmen_zpatky(t):
    pokemon01.image = obrazek
    pyglet.clock.schedule_once(zmen, 1)

pyglet.clock.schedule_once(zmen, 1)

pyglet.app.run()







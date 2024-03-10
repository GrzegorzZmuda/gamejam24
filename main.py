import pyglet
from random import randrange
from pyglet.window import key
from math import sqrt
from pyglet import shapes

window = pyglet.window.Window(width=1300, height=700)
keys = key.KeyStateHandler()
window.push_handlers(keys)
start=False
sine = pyglet.media.synthesis.Sine(0.3, frequency=440, sample_rate=44800)
pter_img = pyglet.resource.image('otter.png')
pter = pyglet.sprite.Sprite(pter_img, x=30, y=100)
Stor_img = pyglet.resource.image('Stor.png')
Stroid_img = pyglet.resource.image('Stroid.png')
Voidstroid_img = pyglet.resource.image('VoidStroid.png')
Dangstroid_img = pyglet.resource.image('DangStroid.png')
line = shapes.Line(30, 100, 100, 500, 2, color = (255, 100, 100))
stors=[]
for i in range(30):
    stors.append(pyglet.sprite.Sprite(Stor_img, x=randrange(0,1300), y=randrange(100,600)))
pter = pyglet.sprite.Sprite(pter_img, x=30, y=100)
stroids=[]
for i in range(5):
    stroids.append(pyglet.sprite.Sprite(Stroid_img, x=randrange(700,1300), y=randrange(0,700)))
voidstroids=[]
for i in range(7):
    voidstroids.append([pyglet.sprite.Sprite(Voidstroid_img, x=randrange(700,1300), y=randrange(0,700)),randrange(0,2)])
dangstroids = []
for i in range(2):
    dangstroids.append(pyglet.sprite.Sprite(Dangstroid_img, x=randrange(700,1300), y=randrange(0,700)))
@window.event
def on_mouse_motion(x, y, dx, dy):
    line.x2=x
    line.y2=y

@window.event
def on_draw():
    window.clear()
    pter.y=pter.y-1
    if keys[key.W]:
        pter.y=pter.y+6
    elif keys[key.S]:
        pter.y = pter.y - 8
    for i in stors:
        i.x=i.x-3
        i.draw()
        if i.x<0:
            i.x=1305
            i.y=randrange(100,700)
    for i in stroids:
        i.x=i.x-7
        i.draw()
        if i.x<0:
            i.x=randrange(1305,1600)
            i.y=randrange(0,700)
    for i in dangstroids:
        i.x=i.x-13
        i.draw()
        if i.x<0:
            i.x=randrange(1305,1600)
            i.y=randrange(0,700)
    for i in voidstroids:
        i[0].x=i[0].x-5
        i[0].draw()
        if i[0].x<0:
            i[1]=randrange(0,2)
            i[0].x=randrange(1305,1600)
            i[0].y=randrange(0,700)
    pter.draw()
    line.x=pter.x+75
    line.y=pter.y+7
    line.x2=line.x2
    line.y2=line.y2
    line.draw()
    for i in stroids:
        if sqrt((pter.x-i.x)*(pter.x-i.x)+(pter.y-i.y)*(pter.y-i.y))<50:
            pyglet.app.exit()
    changed=False
    for i in voidstroids:
        print(sqrt((line.x2-i[0].x)*(line.x2-i[0].x)+(line.y2-i[0].y)*(line.y2-i[0].y))<80 and i[1]>0)
        print(sqrt((line.x2 - i[0].x) * (line.x2 - i[0].x) + (line.y2 - i[0].y) * (line.y2 - i[0].y)))
        if sqrt((line.x2-i[0].x)*(line.x2-i[0].x)+(line.y2-i[0].y)*(line.y2-i[0].y))<60 and i[1]>0:
            sine.play()
            changed=True
        elif not changed:
            pass
        if (sqrt((pter.x-i[0].x+35)*(pter.x-i[0].x+35)+(pter.y-i[0].y+10)*(pter.y-i[0].y+10))<30 and i[1]>0) or pter.y<-50 :
            pyglet.app.exit()

pyglet.app.run()
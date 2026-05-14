import pygame as py
from pygame.locals import *
import sys
import numpy
py.init()
scalefactor = 50
Screen = py.display.set_mode([16*scalefactor, 16*scalefactor])
playerimage = py.image.load("Player.png")
playerimage = py.transform.scale(playerimage, (scalefactor, scalefactor)).convert_alpha()
appleimage = py.image.load("Apple.png")
appleimage = py.transform.scale(appleimage, (scalefactor, scalefactor))
xd = 0
yd = 0
position = (0, 0)
FPS = py.time.Clock()
while True:
    FPS.tick(10)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    keypressed = py.key.get_pressed()
    if yd != scalefactor:  
        if keypressed[K_UP]:
            yd = -scalefactor  # ⬆ Also note: UP should decrease y, not increase it
            xd = 0
    if yd != -scalefactor:
        if keypressed[K_DOWN]:
            yd = scalefactor
            xd = 0
    if xd != -scalefactor:
        if keypressed[K_RIGHT]:
            xd = scalefactor
            yd = 0
    if xd != scalefactor:
        if keypressed[K_LEFT]:
            xd = -scalefactor
            yd = 0
    position = (position[0] + xd, position[1] + yd)
    Screen.fill([255, 255, 255])
    Screen.blit(playerimage, [position[0], position[1]])
    Screen.blit(appleimage, [8*scalefactor, 12*scalefactor])
    py.display.flip()   

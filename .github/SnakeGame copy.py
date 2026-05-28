import pygame as py
from pygame.locals import *
import sys
import numpy
import random
py.init()

taildic = {

}

scalefactor = 50
Screen = py.display.set_mode([16*scalefactor, 16*scalefactor])
playerimageright = py.image.load("Player-Right.png")
playerimageright = py.transform.scale(playerimageright, (scalefactor, scalefactor)).convert_alpha()
playerimageleft = py.image.load("Player-Left.png")
playerimageleft = py.transform.scale(playerimageleft, (scalefactor, scalefactor)).convert_alpha()
playerimagerighttail = py.image.load("Player-Tail-Right.png")
playerimagerighttail = py.transform.scale(playerimagerighttail, (scalefactor, scalefactor)).convert_alpha()
playerimagelefttail = py.image.load("Player-Tail-Left.png")
playerimagelefttail = py.transform.scale(playerimagelefttail, (scalefactor, scalefactor)).convert_alpha()
appleimage = py.image.load("Apple.png")
appleimage = py.transform.scale(appleimage, (scalefactor, scalefactor))
xd = 0
yd = 0
direction = ""
position = (scalefactor, scalefactor)
FPS = py.time.Clock()
count = 0
frame = 0
history = [

]
historicaldirection = [

]
class Tail:
    def __init__(self):
        self.playerimagerighttail = py.image.load("Player-Tail-Right.png")
        self.playerimagerighttail = py.transform.scale(playerimagerighttail, (scalefactor, scalefactor)).convert_alpha()
        self.playerimagelefttail = py.image.load("Player-Tail-Left.png")
        self.playerimagelefttail = py.transform.scale(playerimagelefttail, (scalefactor, scalefactor)).convert_alpha()
    def draw(self, position, direction):
        if direction == "right":
            self.playerimagerighttail = py.image.load("Player-Tail-Right.png")
            self.playerimagerighttail = py.transform.scale(playerimagerighttail, (scalefactor, scalefactor)).convert_alpha()
            Screen.blit(playerimagerighttail, position)
        elif direction == "left":
            self.playerimagelefttail = py.image.load("Player-Tail-Left.png")
            self.playerimagelefttail = py.transform.scale(playerimagelefttail, (scalefactor, scalefactor)).convert_alpha()
            Screen.blit(playerimagelefttail, position)

appleposition = (8*scalefactor, 8*scalefactor)
def startApple():
    global appleposition 
    appleposition = (8*scalefactor, 8*scalefactor)
def newApple():
    global appleposition 
    appleposition = (random.randint(0, 15)*scalefactor, random.randint(0, 15)*scalefactor)
istail= False

while True:
    recievedinput = False
    FPS.tick(12)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
                if recievedinput == False:
                    if yd != scalefactor:  
                        if event.key == K_UP:
                            yd = -scalefactor  # Also note: UP should decrease y, not increase it
                            xd = 0
                            recievedinput = True
                    if yd != -scalefactor:
                        if event.key == K_DOWN:
                            yd = scalefactor
                            xd = 0
                            recievedinput = True
                    if xd != -scalefactor:
                        if event.key == K_RIGHT:
                            xd = scalefactor
                            yd = 0
                            recievedinput = True
                    if xd != scalefactor:
                        if event.key == K_LEFT:
                            xd = -scalefactor
                            yd = 0
                            recievedinput = True
    position = (position[0] + xd, position[1] + yd)
    Screen.fill([255, 255, 255])
    if xd == scalefactor:
        direction = "right"
    if xd == -scalefactor:
        direction = "left"
    if direction == "right":
        Screen.blit(playerimageright, [position[0], position[1]])
    if direction == "left":
        Screen.blit(playerimageleft, [position[0], position[1]])
    if count == 0:
        startApple()
    if position == appleposition:
        count += 1
        newApple()
        while appleposition in taildic:
            newApple()
        taildic[count]= Tail()
        istail = True
    if istail == True:
        for i in taildic:
            taildic[i].draw(history[frame-i], historicaldirection[frame-i])
            if history[frame-i] == position:
                py.quit()
                sys.exit()
    Screen.blit(appleimage, appleposition)
    history.append(position)
    historicaldirection.append(direction)
    frame += 1
    if position[0]>=17*scalefactor or position[1]>=17*scalefactor or position[0] <= -1 or position[1] <= -1:
        py.quit()
        sys.exit()

    py.display.flip()   

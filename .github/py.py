import pygame as py
from pygame.locals import *
import sys
import random

py.init()
 
FPS = 60
FramePerSec = py.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

displayscreen = py.display.set_mode((300, 300), flags = py.RESIZABLE)
displayscreen.fill(WHITE)
py.display.set_caption("Game")


object1 = py.Rect((20, 50), (50, 100))
object2 = py.Rect((10, 10), (100, 100))

print(object1.colliderect(object2))
FPS = py.time.Clock()
FPS.tick(66)
py.init()


class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (150, 150)
        self.direction = (0, 0)
    def update(self):
        pressed_keys = py.key.get_pressed()
        if pressed_keys[K_UP]:
            if self.direction != (0, 1):
                self.direction = (0, -1)
        if pressed_keys[K_DOWN]:
            if self.direction != (0, -1):
                self.direction = (0, 1)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                if self.direction != (1, 0):
                    self.direction = (-1, 0)
        if self.rect.left > 0:       
            if pressed_keys[K_RIGHT]:
                if self.direction != (-1, 0):
                    self.direction = (1, 0)
        self.rect.move_ip(self.direction[0], self.direction[1])

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def move(self):
        self.rect.move_ip(0, 10)
        if(self.rect.top >600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
class Apple(py.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = py.image.load("Apple.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)   

P1 = Player()
A1 = Apple()
while True:
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    displayscreen.fill(WHITE)
    P1.update()
    P1.draw(displayscreen)
    A1.draw(displayscreen)
    py.display.update()

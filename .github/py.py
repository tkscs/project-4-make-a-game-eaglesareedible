import pygame as py
from pygame.locals import *
import sys
import random, time
import numpy

py.init()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

displayscreen = py.display.set_mode((320, 320), flags = py.RESIZABLE)
displayscreen.fill(BLACK)
py.display.set_caption("Game")


object1 = py.Rect((20, 50), (50, 100))
object2 = py.Rect((10, 10), (100, 100))

print(object1.colliderect(object2))
FPS = py.time.Clock()
py.init()
scalefactor = 20/66

apple = [60, 60]
class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.direction = (0, 0)
        self.position = numpy.array([160, 160])
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
        self.position += numpy.array(self.direction)
        self.rect.center = (int(self.position[0])*scalefactor, int(self.position[1])*scalefactor)
        #self.rect.move_ip(int(self.position[0])*scalefactor, int(self.position[1])*scalefactor)
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
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(40,SCREEN_WIDTH-40))
    def draw(self, surface):
        surface.blit(self.image, self.rect)   

P1 = Player()
A1 = Apple()
apples = py.sprite.Group()
apples.add(A1)
all_sprites = py.sprite.Group()
all_sprites.add(P1)
all_sprites.add(A1)

while True:
    count = 0
    FPS.tick(66)
    fps = FPS.get_fps()
    if fps > 0:
        scalefactor = 40/fps
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()
    displayscreen.fill(BLACK)
    P1.update()
    P1.draw(displayscreen)
    A1.draw(displayscreen)
    if FPS.get_fps() != 66:
        print(FPS.get_fps())
    if py.sprite.spritecollideany(P1, apples):
        py.display.update()
        A1.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(40,SCREEN_WIDTH-40))
        count +=1

    py.display.update()

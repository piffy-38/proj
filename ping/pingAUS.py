from time import *
from time import time as timer
from random import randint
from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QLabel, QRadioButton, QHBoxLayout, QPushButton, QVBoxLayout, QMessageBox, QGroupBox
mixer.init()
font.init()
font = font.Font(None, 36)
pL_lose = font.render('ИГРОК 1 ПРОИГРАЛ', True, (200, 0, 0))
win_width = 700
win_height = 500
clock = time.Clock()
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('bak.jpg'), (win_width,win_height))
fps = 60
lost = 0
a = True
b = 0
c = 0
print(b)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-200:
            self.rect.y += self.speed
class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-200:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        global a
        global b
        global c 
        if sprite.collide_rect(ball, player2):
            a = True
            print(a)
            rand = randint(1,2)
            print(rand)
            if rand == 1:
                b = 1
            if rand == 2:
                b = 2
        if sprite.collide_rect(ball, wall1):
            b = 3
            self.rect.y += self.speed
            self.rect.x -= self.speed
        if sprite.collide_rect(ball, wall2):
            rand2 = randint(10,11)
            if rand2 == 10:
                c = 2
            if rand2 == 11:
                c = 3
            b = 6
            self.rect.y -= self.speed
            self.rect.x += self.speed
            print(b)
        elif a == True and b == 0:
            self.rect.x += self.speed
        elif a == True and b == 1:
            self.rect.y -= self.speed
            self.rect.x -= self.speed
        elif a == True and b == 2:
            self.rect.y += self.speed
            self.rect.x -= self.speed
        elif a == True and b == 3:
            self.rect.y += self.speed
            self.rect.x -= self.speed
        elif a == True or a == False and b == 6:
            self.rect.y -= self.speed
            if c == 2:
                self.rect.x -= self.speed
            if c == 3:
                self.rect.x += self.speed
            
        

    def update2(self):
        global a
        global b
        global c
        if sprite.collide_rect(ball, player1):
            a = False
            print(a)
            rand = randint(3,4)
            print(rand)
            if rand == 3:
                b = 3
            if rand == 4:
                b = 4
            print(b)
        if sprite.collide_rect(ball, wall1):
            rand2 = randint(10,11)
            if rand2 == 10:
                c = 2
            if rand2 == 11:
                c = 3
            b = 3
            self.rect.y += self.speed
            self.rect.x -= self.speed
        #if sprite.collide_rect(ball, wall2):
            #b = 6
            #self.rect.y -= self.speed
            #self.rect.x += self.speed
            #print(b)
        elif a == False and b == 0:
            self.rect.x -= self.speed
        elif a == False and b == 3:
            self.rect.y += self.speed
            self.rect.x += self.speed
        elif a == False and b == 4:
            self.rect.y -= self.speed
            self.rect.x += self.speed

        

        
        


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


        
        













player1 = Player_1('player1.png', 10, 320, 25, 200, 10)
player2 = Player_2('player2.png', 650, 320, 75, 200, 10)
ball = Ball('bal.png', 150, 250, 50, 50, 5)
wall1 = Wall(255, 255, 255, -19, -19, 750, 20)
wall2 = Wall(255, 255, 255, 0, 499, 750, 20)

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0,0))


        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        ball.update2()
        wall1.draw_wall()
        wall2.draw_wall()
        

        display.update()
        clock.tick(fps)
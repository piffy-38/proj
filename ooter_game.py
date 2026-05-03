
# -*- coding: utf-8 -*-
from time import *
from time import time as timer
from random import randint
from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QLabel, QRadioButton, QHBoxLayout, QPushButton, QVBoxLayout, QMessageBox, QGroupBox
mixer.init()
font.init()
mixer.music.load('GTA2.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
pain = mixer.Sound('dsplpain.wav')
DOOM = mixer.Sound('only.mp3')
shotgun_shell = mixer.Sound('shotgun.mp3')

win_width = 700
win_height = 500
app = QApplication([])
window = display.set_mode((win_width,win_height))
display.set_caption('gta_light, для вызова меню управления нажмите c')
background = transform.scale(image.load('city.png'), (win_width,win_height))
fail = transform.scale(image.load('fail.png'), (win_width,win_height))
FPS = 60
hp = 100
clock = time.Clock()

msg = QMessageBox()
msg.setWindowTitle("УПРАВЛЕНИЕ")
msg.setText("ПАУЗА - P\nУПРАВЛЕНИЕ ЗВУКОМ: 0-5 - ГРОМКОСТЬ, R - СБРОСИТЬ ДО ОРИГИНАЛЬНОГО ЗНАЧЕНИЯ \nВЛЕВО/ВПРАВО - СТРЕЛОЧКИ ВЛЕВО, ВПРАВО \n ВВЕРХ/ВНИЗ - СТРЕЛОЧКИ ВВЕРХ, ВНИЗ \n СТРЕЛЯТЬ - SPACE \n УПРАВЛЕНИЕ - С \n АКТИВАЦИЯ ЧИТ-ФУНКЦИЙ - X")

msg2 = QMessageBox()
msg2.setWindowTitle("You've found the silly cat!")
msg2.setText(' ⣼⠲⢤⡀⣀⣐⣷⢤⡀⠀⠀⠀⠀⢀⣀⠀\n  ⡇⠀⠀⠘⠷⣀⠀⠀⠈⢻⢤⠶⠛⠉⢸⡇\n ⠸⡁⠀⢀⣠⣄⠀⠀⠀⡀⣀⠀⠀⠀⠀⡾⠁\n⢀⡀⣇⢰⡟⢰⣿   ⣼⡇⠈⠳⡄⠀⣰⠃\n⠙⢧⡀⠸ ⢘⣛⡀⠀⠻⠇⠀⣰⠃⢚⣳\n ⠸⠵⠢⣄⣀⠈⣠⡀    ⢉⣠⣿⡁⠀⠀⡀⠀\n    ⢲⣟⠛⠀⠀⠀⠉⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⢀⠀⡏⢳\n⠀⠀⠀⠀⠠⢯⡀⠀⠀⠀⠀⠀⢼⠛⠀⠀⠀⠀⠀⠀⠀⢸⡦⠃⠘\n⠀⠀⠀⠀⠀⢸⡇⠀⠘⣾⠇⠀⠸⣦⠀⠀⠀⠀⠀⠀⠀⣰\n⠀⠀⠀⠀⠀⠀⣶⠀⠀⢻⡆⠀⢸⡇⠉⠲⣄⠀⣀⡀⡶⠃\n⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢸⡇⠀⠀⢹⡏⠁')



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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-85:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-80:
            self.rect.y += self.speed

    def fire(self):
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 20, 20, 20)
            bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            lost += 1
            self.rect.y = 0
            self.rect.x = randint(170, win_width - 180)

class Object(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(170, win_width - 180)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


vol = 1.0
stat_font = font.SysFont('Arial', 36)
winlose_font = font.SysFont('Arial', 72)
lost = 0
killed = 0
win_killed = 15
max_lost = 15
paused = False
num_fire = 0
rel_time = False
rel_sec = 2
cht = False
weap2 = False
weap1 = False

def soundAndButtonControl():
    keys = key.get_pressed()
    if keys[K_1]:
        vol = 0.1
        mixer.music.set_volume(vol)
        f1 = font.Font(None, 36)
        text1 = f1.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 10%', 1, (180, 0, 0))
        window.blit(text1, (100, 100))
    elif keys[K_2]:
        vol = 0.2
        mixer.music.set_volume(vol)
        f2 = font.Font(None, 36)
        text1 = f2.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 20%', 1, (180, 0, 0))
        window.blit(text1, (100, 100))
    elif keys[K_3]:
        vol = 0.3
        mixer.music.set_volume(vol)
        f3 = font.Font(None, 36)
        text3 = f3.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 30%', 1, (180, 0, 0))
        window.blit(text3, (100, 100))
    elif keys[K_4]:
        vol = 0.4
        mixer.music.set_volume(vol)
        f4 = font.Font(None, 36)
        text4 = f4.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 40%', 1, (180, 0, 0))
        window.blit(text4, (100, 100))
    elif keys[K_5]:
        vol = 0.5
        mixer.music.set_volume(vol)
        f5 = font.Font(None, 36)
        text5 = f5.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 50%', 1, (180, 0, 0))
        window.blit(text5, (100, 100))
    elif keys[K_0]:
        vol = 0.0
        mixer.music.set_volume(vol)
        f0 = font.Font(None, 36)
        text0 = f0.render('ИЗМЕНЕНИЕ УРОВНЯ ГРОМКОСТИ: 0%', 1, (180, 0, 0))
        window.blit(text0, (100, 100))
    elif keys[K_c]:
        vol = 0
        msg.exec_()
    elif keys[K_g]:
        vol = 0
        msg2.exec()
    elif keys[K_r]:
        vol = 1.0
        mixer.music.set_volume(vol)
        fr = font.Font(None, 36)
        textr = fr.render('RETURNING TO ORIGINAL STATE OF SOUNDfx', 1, (180, 0, 0))
        window.blit(textr, (100, 100))
    elif keys[K_x]:
        global hp
        hp = 999999
        for i in range(55):
            monster = Enemy('VRAG.png', randint(170, win_width - 180), -40, 65, 65, randint(1,15))
            monsters.add(monster)
        cheat_t = stat_font.render('CHEATS ACTIVATED', 1, (255, 215, 0))
        window.blit(cheat_t, (220,60))
        global cht
        cht = True
        global max_lost
        max_lost = 999999
        global win_killed
        win_killed = 999999
        mixer.music.set_volume(0)
        DOOM.play()
    elif keys[K_7]:
        global weap2
        global weap1
        weap2 = True
        weap1 = False
    elif keys[K_6]:
        weap2 = False
        weap1 = True
    lost_t = stat_font.render('lost: ' + str(lost) + '/' + str(max_lost), 1, (255, 215, 0))
    window.blit(lost_t, (10,110))
    mon_downt = stat_font.render('killed: ' + str(killed) + '/' + str(win_killed), 1, (255, 215, 0))
    window.blit(mon_downt, (10,80))
    hp1 = stat_font.render('HEALTH POINTS:' + str(hp), 1, (255, 0, 0))
    window.blit(hp1, (220,30))



player = Player('SOLDAT.png', 300, 420, 65, 65, 10)
monsters = sprite.Group()
bullets = sprite.Group()
for i in range(5):
    monster = Enemy('VRAG.png', randint(170, win_width - 180), -40, 65, 65, randint(1,5))
    monsters.add(monster)

cars = sprite.Group()
for i in range(3):
    car = Object('car.png', randint(90, win_width - 90), -40, 40, 65, randint(1,3))
    cars.add(car)


 

WIN_T = winlose_font.render('MISSION PASSED!', 1, (255, 215, 0))
LOSE_T = winlose_font.render('PRESS Q TO RESTART', 1, (163, 0, 0))
pause_text = winlose_font.render('ПАУЗА', 1, (0, 0, 0))
hint = stat_font.render('TO EQUIP A WEAPON, PRESS <6> OR <7> KEYS', 1, (184,183,153))
game = True


finish = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if weap1 == True:
                    if num_fire < 5 and rel_time == False:
                        num_fire += 1
                        player.fire()
                        fire_sound.set_volume(1)
                        fire_sound.play()
                    if num_fire >= 5 and rel_time == False:
                        start_time = timer()
                        rel_time = True
                if cht == True:
                    player.fire()
                if weap2 == True:
                        fire_sound.set_volume(0)
                        shotgun_shell.play()
                        bullet1 = Bullet('bullet.png', (player.rect.centerx+30), player.rect.top, 20, 20, 20)
                        bullets.add(bullet1)
                        bullet2 = Bullet('bullet.png', (player.rect.centerx-30), player.rect.top, 20, 20, 20)
                        bullets.add(bullet2)
                        bullet3 = Bullet('bullet.png', (player.rect.centerx), player.rect.top, 20, 20, 20)
                        bullets.add(bullet3)
            if e.key == K_p:
                if paused == True:
                    finish = False
                    paused = False
                    mixer.music.set_volume(1)
                else:
                    finish = True
                    paused = True
                    mixer.music.set_volume(0)




    if not finish:
        window.blit(background, (0,0))
        cars.draw(window)
        cars.update()
        monsters.draw(window)
        bullets.draw(window)
        player.reset()
        player.update()
        monsters.update()
        bullets.update()
        soundAndButtonControl()


        if rel_time == True:
            end_time = timer()

            if end_time - start_time < rel_sec:
                rel_t = stat_font.render('reloading...', 1, (255, 0, 0))
                window.blit(rel_t, (175, 330))
            else:
                num_fire = 0
                rel_time = False
        if weap1 == False and weap2 == False:
            window.blit(hint, (60, 60))
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for collide in sprites_list:
            killed += 1
            monster = Enemy('VRAG.png', randint(170, win_width - 180), -40, 65, 65, randint(2,10))
            monsters.add(monster)
        if killed >= win_killed:
            finish = True
            window.blit(background, (0,0))
            window.blit(WIN_T, (250, 250))
            mixer.music.set_volume(0)
        if sprite.spritecollide(player, monsters, False):
            hp -= 1
            pain.set_volume(0.1)
            pain.play()
        if sprite.spritecollide(player, cars, False):
            hp -= 100
            pain.set_volume(0.1)
            pain.play()
        if lost >= max_lost or hp <= 0:
            finish = True
            mixer.music.set_volume(0)
            window.blit(fail, (0,0))
            window.blit(LOSE_T, (100, 250))
        display.update()
        clock.tick(FPS)
    else:
        keys = key.get_pressed()
        if keys[K_q]:
            lost = 0
            killed = 0
            hp = 100
            max_lost = 15
            num_fire = 0
            weap2 = False
            weap1 = False
            for monster in monsters:
                monster.kill()
            for bullet in bullets:
                bullet.kill()
            for car in cars:
                car.kill()
            for i in range(5):
                monster = Enemy('VRAG.png', randint(170, win_width - 180), -40, 65, 65, randint(1,5))
                monsters.add(monster)
            for i in range(3):
                car = Object('car.png', randint(90, win_width - 90), -40, 40, 65, randint(1,3))
                cars.add(car)
            window.blit(background, (0,0))
            mixer.music.set_volume(1)
            mixer.music.play()
            finish = False

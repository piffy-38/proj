from time import *
from time import time as timer
from random import randint
from pygame import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QLabel, QRadioButton, QHBoxLayout, QPushButton, QVBoxLayout, QMessageBox, QGroupBox, QInputDialog
mixer.init()
font.init()
menumusic = mixer.Sound('ping/MENU.mp3')
paused = mixer.Sound('ping/PAUSED.mp3')
ingame = mixer.Sound('ping/INGAME.mp3')
bounce1 = mixer.Sound('ping/Discord Push To Talk; Active Sound Effect (HD) (2).mp3')
bounce2 = mixer.Sound('ping/Discord Push To Talk; Deactivate Sound Effect (HD) (2).mp3')
button_click = mixer.Sound('ping/Button Press Sound Effect (Free Use) (mp3cut.net).mp3')
warn = mixer.Sound('ping/Skype - All Old Sounds (mp3cut.net).mp3')
stat_font = font.SysFont('Arial', 36)
winlose_font = font.SysFont('Arial', 72)
pL_lose = stat_font.render('ИГРОК 1 ПРОИГРАЛ', True, (200, 0, 0))
win_width = 700
win_height = 500
clock = time.Clock()
window = display.set_mode((win_width,win_height))
background = transform.scale(image.load('ping/bak.jpg'), (win_width,win_height))
background2 = transform.scale(image.load('ping/DSC_0486.jpg'), (win_width,win_height))
background3 = transform.scale(image.load('ping/photo_2025-03-14_18-19-51.jpg'), (win_width,win_height))
background4 = transform.scale(image.load('ping/photo_2025-05-08_22-40-26.jpg'), (win_width,win_height))
background5 = transform.scale(image.load('ping/avatars-linrvoMB2op3z8kV-bOyWUg-t240x240.jpg'), (win_width,win_height))
app = QApplication([])
xuindow = QWidget()
ask1 = QInputDialog()
ask2 = QInputDialog()
display.set_caption('САМАЯ ЛУЧШАЯ КЛАССНАЯ ИГРА 100% КЛУБНЯК 2007')

#счётчикиНЕ ТРОГАТЬ
fps = 60
lost = 0
a = True
b = 0
c = 0
d = randint(1,2)
fail1=0
fail2=0
finish = True
game = True
set_clicked = False
gamecont = False
vol = 0.5
vol_counter = 5
player1_name = 'EXAMPLE1'
player2_name = 'EXAMPLE2'
diff_count = 0
difficulty = "Normal"
music = 0
back = randint(0,4)







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
        if difficulty == "Easy":
            self.speed = 20
        if difficulty == "Normal":
            self.speed = 10
        if difficulty == "Hard":
            self.speed = 7.5
        if keys[K_UP] and self.rect.y > 55:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500-200:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if difficulty == "Easy":
            self.speed = 20
        if difficulty == "Normal":
            self.speed = 10
        if difficulty == "Hard":
            self.speed = 7.5
        if keys[K_w] and self.rect.y > 55:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500-200:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global a
        global b
        global c 
        if difficulty == "Easy":
            self.speed = 5
        if difficulty == "Normal":
            self.speed = 12.5
        if difficulty == "Hard":
            self.speed = 20
        if sprite.collide_rect(ball, player2):
            a = True
            bounce1.play()
            rand = randint(1,2)
            if rand == 1:
                b = 1
            if rand == 2:
                b = 2
        if sprite.collide_rect(ball, wall1):
            bounce2.play()
            b = 3
            self.rect.y += self.speed
            self.rect.x -= self.speed
        if sprite.collide_rect(ball, wall2):
            bounce2.play()
            rand2 = randint(10,11)
            if rand2 == 10:
                c = 2
            if rand2 == 11:
                c = 3
            b = 6
            self.rect.y -= self.speed
            self.rect.x += self.speed
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
        global d
        if sprite.collide_rect(ball, player1):
            a = False
            bounce1.play()
            rand = randint(3,4)
            if rand == 3:
                b = 3
            if rand == 4:
                b = 4
        if sprite.collide_rect(ball, wall1):
            bounce2.play()
            rand2 = randint(10,11)
            if rand2 == 10:
                c = 2
            if rand2 == 11:
                c = 3
            b = 3
            self.rect.y += self.speed
            self.rect.x -= self.speed
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
class Button():
    def __init__(self, x=0, y=0, width=5, height=5, color=(255,255,255)):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def set_text(self, text, fsize=18, text_color = (0, 0, 0)):
        self.text = text
        self.image = font.Font(None, fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    def collide_point(self, x, y):
        return self.rect.collidepoint(x, y)

msg = QMessageBox()
msg.setWindowTitle("Error!")
msg.setText("Enter Players Names in settings first!")
volume = stat_font.render('Music volume', 1, (255, 255, 255))
volume_counter = stat_font.render(str(vol_counter), 1, (255, 255, 255))
pname = stat_font.render('Players Names', 1, (255, 255, 255))
diff = stat_font.render('Difficulty', 1, (255, 255, 255))
diff_counter = stat_font.render(difficulty, 1, (145, 126, 31))
p1name = stat_font.render('Player 1:', 1, (255, 0, 0))
p2name = stat_font.render('Player 2:', 1, (255, 0, 0))
player1 = Player_1('ping/player1.png', 10, 320, 25, 200, 10)
player2 = Player_2('ping/player2.png', 650, 320, 75, 200, 10)
ball = Ball('ping/bal.png', 150, 250, 50, 50, 10)
wall1 = Wall(0, 0, 0, 0, -50, 750, 20)
wall2 = Wall(255, 255, 255, 0, 500, 750, 20)
btn_start = Button(270, 325, 200, 50)
btn_start.set_text('1')
btn_set = Button(270, 200, 200, 50)
btn_set.set_text('Settings', 55)
btn_volumeUP = Button(50, 50, 25, 25)
btn_volumeDOWN = Button(125, 50, 25, 25)
btn_BACK = Button(10, 10, 40, 40)
btn_BACKtoMAIN = Button(0, 460, 40, 40)
btn_p1name = Button(130, 128, 25, 25)
btn_p2name = Button(130, 168, 25, 25)
btn_diffUP = Button(480, 55, 25, 25)
btn_diffDOWN = Button(650, 55, 25, 25)
btn_BACK.set_text('<-')
btn_BACKtoMAIN.set_text('<<-')
btn_volumeUP.set_text('+')
btn_volumeDOWN.set_text('-')
btn_p1name.set_text('Ent_')
btn_p2name.set_text('Ent_')
btn_diffUP.set_text('+')
btn_diffDOWN.set_text('-')
#текст1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if finish == True and set_clicked == False:
                if btn_start.collide_point(x, y):
                    button_click.play()
                    if player1_name == 'EXAMPLE1' and player2_name == 'EXAMPLE2':
                        warn.play()
                        msg.exec()
                    else:
                        finish = False
                if btn_set.collide_point(x, y):
                    button_click.play()
                    set_clicked = True
            if finish == True and set_clicked == True:
                if btn_BACK.collide_point(x, y):
                    button_click.play()
                    set_clicked = False
                if btn_volumeDOWN.collide_point(x,y):
                    button_click.play()
                    vol -= 0.1
                    vol_counter -= 1
                    menumusic.set_volume(vol)
                    ingame.set_volume(vol)
                    if vol < 0:
                        vol = 0
                        vol_counter = 0
                    volume_counter = stat_font.render(str(vol_counter), 1, (255, 255, 255))
                if btn_volumeUP.collide_point(x,y):
                    button_click.play()
                    vol += 0.1
                    vol_counter += 1
                    if vol > 0.91:
                        vol = 1
                        vol_counter = 10
                    menumusic.set_volume(vol)
                    ingame.set_volume(vol)
                    volume_counter = stat_font.render(str(vol_counter), 1, (255, 255, 255))
                if btn_p1name.collide_point(x,y):
                    button_click.play()
                    p1, ok = ask1.getText(xuindow, 'Player 1', 'Enter Player Name')
                    if ok and p1:
                        player1_name = str(p1)
                if btn_p2name.collide_point(x,y):
                    button_click.play()
                    p2, ok = ask2.getText(xuindow, 'Player 2', 'Enter Player 2 Name')
                    if ok and p2:
                        player2_name = str(p2)
                    #здесь p1 и ok отвечают за 2 типа данных, которые выдает .getText - p1 это string, ok - True или False,
                    #ok мне не нужна, и поэтому я просто беру и печатаю p1 которая забрала в себя строку, введеную пользователем
                if btn_diffUP.collide_point(x,y):
                    button_click.play()
                    diff_count += 1
                    if diff_count > 2:
                        diff_count = 2
                    if diff_count == 0:
                        difficulty = "Easy"
                    if diff_count == 1:
                        difficulty = "Normal"
                    if diff_count == 2:
                        difficulty = "Hard"
                    diff_counter = stat_font.render(difficulty, 1, (145, 126, 31))
                if btn_diffDOWN.collide_point(x,y):
                    button_click.play()
                    diff_count -= 1
                    if diff_count < 0:
                        diff_count = 0
                    if diff_count == 0:
                        difficulty = "Easy"
                    if diff_count == 1:
                        difficulty = "Normal"
                    if diff_count == 2:
                        difficulty = "Hard"
                    diff_counter = stat_font.render(difficulty, 1, (145, 126, 31))
            if finish == True and gamecont == True and set_clicked == False:
                if btn_BACKtoMAIN.collide_point(x,y):
                    button_click.play()
                    lost = 0
                    a = True
                    b = 0
                    c = 0
                    fail1=0
                    fail2=0
                    finish = True
                    game = True
                    set_clicked = False
                    ball_speed = 10
                    gamecont = False
                    vol = 0
                    player1.rect.x = 10 
                    player1.rect.y = 320
                    player2.rect.x = 650
                    player2.rect.y = 320
                    ball.rect.x = 150
                    ball.rect.y = 250
                    difficulty = "Normal"
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                finish = True

    hp1 = stat_font.render(player1_name + ':' + str(fail1), 1, (255, 0, 0))
    hp2 = stat_font.render(player2_name + ':' + str(fail2), 1, (255, 0, 0))
    if finish == False:
        vol = 0.5
        if back == 0:
            window.blit(background, (0,0))
        elif back == 1:
            window.blit(background2, (0,0))
        elif back == 2:
            window.blit(background3, (0,0))
        elif back == 3:
            window.blit(background4, (0,0))
        elif back == 4:
            window.blit(background5, (0,0))
        else:
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
        window.blit(hp1, (20,0))
        window.blit(hp2, (450, 0))
        gamecont = True

        if ball.rect.x < 0:
            a = True
            b = 0
            c = 0
            ball.rect.x = 150
            ball.rect.y = 250
            fail1 += 1
            hp1 = stat_font.render(player1_name + ':' + str(fail1), 1, (255, 0, 0))
            text0 = winlose_font.render('FAILED!', 1, (180, 0, 0))
            window.blit(text0, (100, 100))
        if ball.rect.x > 700:
            a = True
            b = 0
            c = 0
            ball.rect.x = 150
            ball.rect.y = 250
            fail2 += 1
            hp2 = stat_font.render(player2_name + ':' + str(fail2), 1, (255, 0, 0))
            text1 = winlose_font.render('FAILED!', 1, (180, 0, 0))
            window.blit(text1, (100, 100))
        if fail1 > 10 or fail2 > 10:
            finish = True
            lost = 0
            a = True
            b = 0
            c = 0
            fail1=0
            fail2=0
            finish = True
            game = True
            set_clicked = False
            ball_speed = 10
            gamecont = False
            vol = 0
            player1.rect.x = 10 
            player1.rect.y = 320
            player2.rect.x = 650
            player2.rect.y = 320
            ball.rect.x = 150
            ball.rect.y = 250
            difficulty = "Normal"
    else:
        if set_clicked == False and gamecont == False:
            if back == 0:
                window.blit(background, (0,0))
            elif back == 1:
                window.blit(background2, (0,0))
            elif back == 2:
                window.blit(background3, (0,0))
            elif back == 3:
                window.blit(background4, (0,0))
            elif back == 4:
                window.blit(background5, (0,0))
            else:
                window.blit(background, (0,0))
            btn_start.set_text('Start the game', 38)
            menu_text = winlose_font.render('Menu', 1, (180, 0, 0))
            window.blit(menu_text, (300, 50))
            btn_start.draw()    
            btn_set.draw()
        if set_clicked == False and gamecont == True:
            if back == 0:
                window.blit(background, (0,0))
            elif back == 1:
                window.blit(background2, (0,0))
            elif back == 2:
                window.blit(background3, (0,0))
            elif back == 3:
                window.blit(background4, (0,0))
            elif back == 4:
                window.blit(background5, (0,0))
            else:
                window.blit(background, (0,0))
            btn_start.set_text('Continue?', 52)
            menu_text = winlose_font.render('PAUSED', 1, (180, 0, 0))
            window.blit(menu_text, (250, 50))
            btn_start.draw()    
            btn_set.draw()
            btn_BACKtoMAIN.draw()
        if set_clicked == True:
            if back == 0:
                window.blit(background, (0,0))
            elif back == 1:
                window.blit(background2, (0,0))
            elif back == 2:
                window.blit(background3, (0,0))
            elif back == 3:
                window.blit(background4, (0,0))
            elif back == 4:
                window.blit(background5, (0,0))
            else:
                window.blit(background, (0,0))
            btn_volumeUP.draw()
            btn_volumeDOWN.draw()
            btn_BACK.draw()
            btn_p1name.draw()
            btn_p2name.draw()
            btn_diffUP.draw()
            btn_diffDOWN.draw()
            window.blit(volume, (5, 80))
            window.blit(volume_counter, (90,43))
            window.blit(pname, (5, 200))
            window.blit(p1name, (5,115))
            window.blit(p2name, (5,155))
            window.blit(diff, (530, 80))
            window.blit(diff_counter, (525,45))
    if set_clicked == False and gamecont == False and music < 1:
        ingame.stop()
        menumusic.play(-1)
        vol = 0.5
        music += 1
        menumusic.set_volume(vol)
        print(music)
    if finish == False and music == 1:
        music = 0
        menumusic.stop()
        ingame.play(-1)
        print(music)
    if set_clicked == True and gamecont == True and music == 1:
        music = 0
        ingame.stop()
        menumusic.stop()
        paused.play(-1)


    display.update()
    clock.tick(fps)


#звук доделать, кнопки
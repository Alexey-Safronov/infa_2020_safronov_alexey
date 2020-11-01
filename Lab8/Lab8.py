from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import pygame


pygame.init()
pygame.font.init()

FPS = 60
target_time = FPS*120

width = 800
height = 600
font_size = 32
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

DARK_RED = (130, 0, 0)
DARK_BLUE = (0, 0, 130)
DARK_GREEN = (0, 100, 0)
DARK_YELLOW = (100, 100, 0)
DARK_COLORS = [DARK_RED, DARK_BLUE, DARK_GREEN, DARK_YELLOW]

class Ball():
    '''Class Ball has parameters:
    x, y - coordinates of a ball center
    size - radius of a ball
    vx, vy - speed by coordinates
    ay - vertical acceleration
    color'''
    def __init__(self):
        self.x = rnd(100, width - 50)
        self.y = rnd(50, height - 50)
        self.size = rnd(20, 40)
        self.vx = 0
        self.vy = 0
        self.ay = -0.1
        self.color = choice(COLORS)


    def draw(self, surface):
        '''Draw a Ball'''
        pygame.draw.circle(surface, self.color, 
            (int(self.x), int(self.y)), 
            int(self.size)
            )


    def move(self):
        '''Move a Ball'''   
        self.vy = self.vy - self.ay
        if (self.x - self.size <= 0) or (self.x + self.size >= width):
            self.vx = -self.vx
        if (self.y - self.size <= 0) or (self.y + self.size >= height):
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy


    


class Bullet(Ball):
    def __init__(self, Gun):
        Ball.__init__(self)
        self.x = Gun.x_tip
        self.y = Gun.y_tip
        self.size = 10
        self.live = 80
        self.color = DARK_COLORS[rnd(0, 3)]


class Target(Ball):
    def __init__(self):
        Ball.__init__(self)
        self.vx = rnd(-3, 3)
        self.vy = rnd(-3, 3)
        self.live = 500


    def check(self, bullet):
        if (self.x - bullet.x)**2 + (self.y - bullet.y)**2 <= (self.size + bullet.size)**2:
            return True
        else:
            return False


class Gun():
    def __init__(self):
        self.x = 50
        self.y = 500
        self.lenght = 50
        self.x_tip = self 
        self.width = 10
        self.color = BLACK
        self.power = 10
        self.run_on = False
        self.an = 0.1
        self.bullet_list = []
        self.bullet_numb = 10


    def draw(self, surface, mouse_coords, mouse_pressed):
        self.lenght = self.lenght * self.power / 10
        mouse_x, mouse_y = mouse_coords
        self.an = math.atan(
            - (mouse_y - self.y) / (0.000000001 + mouse_x - self.x)
            )
        self.x_tip = self.x + self.lenght * math.cos(self.an)
        self.y_tip = self.y - self.lenght * math.sin(self.an)
        if mouse_pressed:
            self.color = RED
        else:
            self.color = BLACK
        pygame.draw.line(surface, self.color,
            (self.x, self.y),
            (self.x_tip, self.y_tip),
            self.width
            )
        pygame.draw.rect(surface, self.color, (
            self.x - self.width, 
            self.y - self.width,
            int(self.width * 2), 
            int(self.width * 2)
            ))
        self.lenght = 50



    def fire(self, event):
        if self.bullet_numb > 0: 
            self.bullet_numb -= 1
            new_bullet = Bullet(gun)
            event_x, event_y = event.pos
            self.an = math.atan(
                (event_y - new_bullet.y) / (event_x - new_bullet.x))
            new_bullet.vx = self.power * math.cos(self.an)
            new_bullet.vy = self.power * math.sin(self.an)
            self.bullet_list += [new_bullet]
        self.run_on = False
        self.power = 10


    def power_up(self):
        if self.run_on:
            if self.power < 20:
                self.power += 0.1



finished = False
time_counter = 0
gun = Gun()
target_list = []
score = 0

while not finished:
    pygame.time.Clock().tick(FPS)
    screen.fill(WHITE)
    if gun.bullet_numb or gun.bullet_list:
        time_counter += FPS
        if (time_counter % target_time == 0) and (len(target_list) < 5):
            target_list.append(Target())

        for i in range(len(target_list)):
            target_list[i].move()
            target_list[i].draw(screen)
            stop_flag = False
            for j in range(len(gun.bullet_list)):
                if target_list[i].check(gun.bullet_list[j]):
                    stop_flag = target_list[i].check(gun.bullet_list[j])
                    target_list.pop(i)
                    score += 1
                    break
            if stop_flag:
                break

        gun.draw(screen, 
            pygame.mouse.get_pos(), 
            pygame.mouse.get_pressed()[0]
            )
        
        gun.power_up()
        for i in range(len(gun.bullet_list)):
            gun.bullet_list[i].move()
            gun.bullet_list[i].draw(screen)
            gun.bullet_list[i].live -= 1
            if gun.bullet_list[i].live == 0: 
                gun.bullet_list.pop(i)
                break
        screen.blit(
        pygame.font.Font(None, font_size).render(
            'Score: ' + str(score) + '    Ammo: ' + str(gun.bullet_numb), 1, BLACK
            ), 
        (width/2 - font_size*3.5, 100)
        )


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.run_on = True
            elif event.type == pygame.MOUSEBUTTONUP:
                gun.fire(event)

    else:
        screen.blit(
            pygame.font.Font(None, font_size*2).render('Score: ' + str(score), 1, BLACK),
            (width/2 - font_size*2.5, height/2 - font_size*2)
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                
    
    pygame.display.update()


pygame.quit()
pygame.font.quit()
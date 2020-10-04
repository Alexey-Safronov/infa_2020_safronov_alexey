import numpy as np
import pygame 
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
screen.fill((255,255,255))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
circle(screen, color_yellow, (100,100), 100)
rect(screen, color_black, (50, 140, 100, 20), 0)
circle(screen, color_red, (50,75), 25)
circle(screen, color_black, (50,75), 10)
circle(screen, color_red, (150,75), 20)
circle(screen, color_black, (150,75), 10)
polygon(screen, color_black, [(0,20),(20,40),(110,80),(90,60)])
polygon(screen, color_black, [(200,20),(180,40),(90,80),(110,60)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

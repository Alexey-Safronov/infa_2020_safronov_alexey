import pygame
from pygame.draw import *
import numpy as np
pygame.init()

def eskimo(Surface, x, y, size):
	#body 
	ellipse(Surface, brown, (x-80*size, y-75*size, 160*size, 300*size))
	rect(Surface, white, (x - 80*size, y + 75*size, 160*size, 150*size))
	#head
	ellipse(Surface, brown, (x-55*size, y-115*size, 110*size, 65*size))
	ellipse(Surface, grey, (x-37*size, y-108*size, 75*size, 50*size))
	#arms
	ellipse(Surface, brown, (x - 110*size, y - 30*size, 70*size, 30*size))
	ellipse(Surface, brown, (x + 40*size, y - 30*size, 70*size, 30*size))
	#legs
	ellipse(Surface, brown, (x - 50*size, y + 55*size, 40*size, 60*size))
	ellipse(Surface, brown, (x + 10*size , y + 55*size, 40*size, 60*size))
	ellipse(Surface, brown, (x - 70*size, y + 100*size, 60*size, 25*size))
	ellipse(Surface, brown, (x + 10*size, y + 100*size, 60*size, 25*size))
	#clothes
	rect(Surface, darkbrown, (x - 20*size, y - 55*size, 40*size, 110*size))
	rect(Surface, darkbrown, (x - 80*size, y + 55*size, 160*size, 20*size))
	
def cat_with_fish()
	
	




# Constants:
FPS = 30
white = (235, 235, 235)
black = (0, 0, 0)
chromakey = (0, 255, 0)
grey = (192, 192, 192)
red = (255, 120, 115)
yellow = (255, 255, 100)
backcolor = (0, 255, 255)
darkbrown = (108, 93, 83)
brown = (145, 124, 111)
zoom = 12


screen = pygame.display.set_mode((1000, 1000))
eskimo(screen, 500, 500, 1)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
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
	line(Surface, black, (x-17*size, y - 93*size), (x-7*size, y-88*size),3)
	line(Surface, black, (x+18*size, y - 93*size), (x+8*size, y-88*size),3)
	arc(Surface, black, (x-19*size, y - 75*size, 40*size, 10*size), 0, np.pi,3)
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
	#weapon
	line(Surface, black, (x-105*size, y + 100*size), (x-105*size, y-120*size),1)


def cat_with_fish(Surface, x, y, size):
	#body
	ellipse(Surface, grey, (x-70*size, y-15*size, 140*size, 30*size))
	#legs
	ellipse(Surface, grey, (x-70*size, y-5*size, 20*size, 60*size))
	ellipse(Surface, grey, (x-50*size, y-5*size, 20*size, 60*size))
	ellipse(Surface, grey, (x+35*size, y-5*size, 20*size, 60*size))
	ellipse(Surface, grey, (x+55*size, y-5*size, 20*size, 60*size))
	#tail
	ellipse(Surface, grey, (x+40*size, y-7*size, 100*size, 15*size))
	#head
	ellipse(Surface, grey, (x-95*size, y-45*size, 50*size, 40*size))
	#fish
	ellipse(Surface, color_fish, (x - 105*size, y - 25*size, 70*size, 20*size))
	polygon(Surface, color_fish, [(x-35*size,y-15*size), (x-15*size,y-5*size), (x-15*size,y-25*size)])
	circle(Surface, blue,(x - 90*size, y - 15*size), 3)
	polygon(Surface, red, [(x-80*size,y-15*size), (x-60*size,y-15*size), (x-70*size,y+5*size)])
	#eyes
	ellipse(Surface, white, (x-90*size, y-35*size, 15*size, 7*size))
	ellipse(Surface, white, (x-75*size, y-35*size, 15*size, 7*size))
	ellipse(Surface, black, (x-85*size, y-35*size, 5*size, 7*size))
	ellipse(Surface, black, (x-70*size, y-35*size, 5*size, 7*size))
	#ears
	polygon(Surface, grey, [(x-85*size,y-35*size), (x-75*size,y-35*size), (x-80*size,y-52*size)])
	polygon(Surface, grey, [(x-65*size,y-35*size), (x-55*size,y-35*size), (x-60*size,y-52*size)])

def igla(Surface, x, y, size):
	ellipse(Surface, grey, (x-200*size, y - 200*size, 400*size, 400*size))
	arc(Surface, black, (x-200*size, y - 200*size, 400*size, 400*size), 0, np.pi,3)
	#vertical lines
	rect(Surface, white, (x-200*size, y, 400*size, 200*size))
	line(Surface, black, (x-150*size, y - 0*size), (x-150*size, y-135*size),3)
	line(Surface, black, (x-100*size, y - 0*size), (x-100*size, y-170*size),3)
	line(Surface, black, (x-50*size, y - 0*size), (x-50*size, y-190*size),3)
	line(Surface, black, (x-0*size, y - 0*size), (x-0*size, y-200*size),3)
	line(Surface, black, (x+50*size, y - 0*size), (x+50*size, y-190*size),3)
	line(Surface, black, (x+100*size, y - 0*size), (x+100*size, y-170*size),3)
	line(Surface, black, (x+150*size, y - 0*size), (x+150*size, y-135*size),3)
	#horizontal lines
	line(Surface, black, (x-148*size, y - 130*size), (x+148*size, y-130*size),3)
	line(Surface, black, (x-187*size, y - 60*size), (x+187*size, y-60*size),3)
	line(Surface, black, (x-200*size, y), (x + 200*size, y),3)


	

# Constants:
FPS = 30
white = (235, 235, 235)
black = (0, 0, 0)
chromakey = (0, 255, 0)
grey = (204, 204, 204)
red = (255, 120, 115)
yellow = (255, 255, 100)
darkbrown = (108, 93, 83)
color_fish = (147, 172, 167)
brown = (145, 124, 111)
blue = (12, 14, 241)
zoom = 12


screen = pygame.display.set_mode((600, 800))
rect(screen, grey, (0, 0, 600, 350))
rect(screen, white, (0, 350, 600, 450))
igla(screen, 200, 450, 1)
eskimo(screen, 500, 450, 1)
cat_with_fish(screen, 150, 650, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
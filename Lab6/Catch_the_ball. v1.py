import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def create_ball():
    ''' Creates data of new ball
    x, y - center coordinates
    vx, vy - vertical and horizontal speed
    r - radius
    color - color '''
    x = randint(100,500)
    y = randint(100,500)
    vx = randint(-15, 15)
    vy = randint(-15, 15)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    return(x, y, vx, vy, r, color)    
   
def ball(ball_data):
    ''' Moves ball ''' 
    x, y, vx, vy, r, color = ball_data
    x += vx*0.1
    y += vy*0.1
    if (x+r>600) or (x-r<0): 
        vx = -vx
    if (y-r<0) or (y+r>600):
        vy = -vy
    circle(screen, color, (int(x), int(y)), r)
    ball_data = x, y, vx, vy, r, color
    return(ball_data)

def ball_catch(ball_data, event):
    ''' Cheks if we tap on the ball ''' 
    x, y, vx, vy, r, color = ball_data
    event.x, event.y = event.pos
    if (event.x - x)*(event.x - x) + (event.y - y)*(event.y - y) <= r*r: 
        f = True
    else: 
        f = False
    return(f)
 

pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0
score = 0
list_balls = []


while not finished:
    clock.tick(FPS)
    time += 1
    
    if time % 50 == 0:
        list_balls.append(create_ball())

    for i in range(len(list_balls)):
        list_balls[i] = ball(list_balls[i])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True 
            print("Yours score: ", score)
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for i in range(len(list_balls)):
                if ball_catch(list_balls[i], event):
                    score += 1
                    list_balls.pop(i)
                    break
    
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
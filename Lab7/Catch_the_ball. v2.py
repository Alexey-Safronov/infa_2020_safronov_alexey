import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

FPS = 60
screen_width = 600
screen_height = 600

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
    x = randint(100,screen_width - 100)
    y = randint(100,screen_height - 100)
    vx = randint(-15, 15)
    vy = randint(-15, 15)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    return(x, y, vx, vy, r, color)    
   
def create_triangle():
    ''' Creates data of new ball
    x, y - center coordinates
    vx, vy - vertical and horizontal speed
    a - side length
    color - color '''
    x = randint(100,screen_width - 100)
    y = randint(100,screen_height - 100)
    vx = randint(-15, 15)
    vy = randint(-15, 15)
    a = randint(30,50)
    color = COLORS[randint(0, 5)]
    return(x, y, vx, vy, a, color)    
    
def triangle(triangle_data):
    ''' Moves triangle ''' 
    x, y, vx, vy, a, color = triangle_data
    x += vx*0.1
    y += vy*0.1
    if (x+a/2>screen_width) or (x-a/2<0): 
        vx = -vx
    if (y-a*np.sqrt(3)/3<0) or (y+a*np.sqrt(3)/6>screen_height):
        vy = -vy
    polygon(screen, color, [(x - a/2, y + a*np.sqrt(3)/6), (x, y - a*np.sqrt(3)/3), (x + a/2, y + a*np.sqrt(3)/6)])
    triangle_data = x, y, vx, vy, a, color
    return(triangle_data)

def triangle_catch(triangle_data, event):
    ''' Cheks if we tap on the triangle ''' 
    x, y, vx, vy, a, color = triangle_data
    event.x, event.y = event.pos
    if (event.y >= -np.sqrt(3)*event.x + y - a*np.sqrt(3)/3 + np.sqrt(3)*x) and (event.y >= np.sqrt(3)*event.x + y - a*np.sqrt(3)/3 - np.sqrt(3)*x) and (event.y<=y + a*np.sqrt(3)/6): 
        f = True
    else: 
        f = False
    return(f)
 

def ball(ball_data):
    ''' Moves ball ''' 
    x, y, vx, vy, r, color = ball_data
    x += vx*0.1
    y += vy*0.1
    if (x+r>screen_width) or (x-r<0): 
        vx = -vx
    if (y-r<0) or (y+r>screen_height):
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
 
def sort(user_lines):
    '''Do bubble sort by increase elements'''
    for i in range(len(user_lines)):
        A = user_lines[i].split()
        for j in range(len(user_lines)-1):
            A = user_lines[j].split()
            B = user_lines[j+1].split()
            a = int(A[1])
            b = int(B[1])
            if b > a:
                user_lines[j], user_lines[j+1] = user_lines[j+1], user_lines[j]


current_name = input() 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
time = 0
score = 0
list_balls = []
list_triangles = []
file = open("leaderboard.txt", "r")
user_lines = file.readlines()   
file.close()
file = open("leaderboard.txt", "w")
user_score = []


while not finished:
    clock.tick(FPS) 
    time += 1
    
    if time % 50 == 0:
        list_balls.append(create_ball())

    if time % 70 == 0:
        list_triangles.append(create_triangle())


    for i in range(len(list_balls)):
        list_balls[i] = ball(list_balls[i])

    for i in range(len(list_triangles)):
        list_triangles[i] = triangle(list_triangles[i])

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

            for i in range(len(list_triangles)):
                if triangle_catch(list_triangles[i], event):
                    score += 2
                    list_triangles.pop(i)
                    break
    
   
    pygame.display.update()
    screen.fill(BLACK)

user_lines.append(current_name + " " + str(score)) 
sort(user_lines)

for i in range(len(user_lines)):
    file.write(user_lines[i] + '\n')

file.close()
pygame.quit()
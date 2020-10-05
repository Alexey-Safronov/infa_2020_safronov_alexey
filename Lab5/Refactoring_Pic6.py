import pygame, sys
from pygame.draw import *

#Constants  
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 100, 0)
width = 700
height = 500
  
#Creating our main screen(background)
FPS = 30
screen = pygame.display.set_mode((width, height))
screen.fill((255, 160, 122))


def bamboo(x, y, k):
    '''
    Function draws bamboo with leafs
    k - scale factor
    x, y - bamboo coordinates
    '''
   #stem(central)
    
    polygon(screen, green, [(x,y), (x+44/k,y),
                                (x+44/k,y-150/k), (x,y-150/k)]),
    polygon(screen, green, [(x,y-160/k), (x+44/k,y-160/k),
                                (x+44/k,y-310/k), (x,y-310/k)])
    polygon(screen, green, [(x+42/k,y-435/k), (x+72/k, y-435/k),
                                (x+37/k,y-320/k), (x+7/k,y-320/k)])
    polygon(screen, green, [(x+92/k,y-505/k), (x+112/k, y-505/k),
                                (x+67/k,y-445/k), (x+47/k,y-445/k)])
   
    #branches
    arc(screen, green, (int(x+52/k), int(y-385/k), int(200/k), int(250/k)), 1, 3.14, int(4/k))
    arc(screen, green, (int(x+82/k), int(y-505/k), int(400/k), int(150/k)), 1.6, 3.14, int(4/k))   
    arc(screen, green, (int(x-208/k), int(y-305/k), int(200/k), int(250/k)), 0, 2, int(4/k))
    arc(screen, green, (int(x-378/k), int(y-485/k), int(401/k), int(150/k)), 0, 1.6 , int(4/k))
    
    #top left branch
    for i in range(0, 5, 1):
        a = [-158, -120, -88, -183,-50]
        b = [-480, -477, -470, -485, -455]
        leaf(x, y, a[i],b[i],k,-15)
    
    #top right branch
    for i in range(0, 5, 1):
        a = [112, 162, 192, 222, 252]
        b = [-493, -515, -517, -524, -526]
        leaf(x, y, a[i], b[i], k, 15)
        
    #bottom right branch
    for i in range(0, 3,1):
        a = [102, 122,142, -58]
        b = [-395, -405, -408]
        leaf(x, y, a[i], b[i], k, 15)
        
    #bottom left branch
    for i in range(0,3,1):
        a = [-58, -98, -148]
        b = [-253, -295, -306]
        leaf(x, y, a[i], b[i], k, -15)
    

def leaf(x, y, a, b, k, o):
    '''
    Function draws 1 leaf
       
    o - leaf rotate angle
    а - coordinate relativly x
    b - coordinate relativly y
    '''
    surface1 = pygame.Surface([100 / k,100 / k], pygame.SRCALPHA, 32)
    surface1 = surface1.convert_alpha()
    surface2 = pygame.transform.rotate(surface1, o)
    ellipse = pygame.draw.ellipse(surface1, green, (0, 0, 15 / k, 55 / k))
    surface2 = pygame.transform.rotate(surface1, o)
    screen.blit(surface2, (x + a / k, y + b / k))

def panda(x, y, k):
    '''
    Function draws panda on screen
    x, y - coordinates top left point of body
    '''
    body(x, y, k)
    middle_paw(x, y, k)
    right_paw(x, y, k)
    left_paw(x, y, k)
    head(x, y, k)
    ears(x, y, k)
    nose_and_eyes(x, y, k)
  
def body(x, y, k):
    '''
    Function draws panda's body
    '''
    ellipse(screen, white, (x, y, 300/k, 200/k))

def middle_paw(x, y, k):
    '''
    Function draws panda's middle paw
    '''
    surf1 = pygame.Surface((500/k, 500/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((500/k, 500/k), pygame.SRCALPHA)
    ellipse(surf1, black, (0/k, 75/k, 200/k, 400/k))
    ellipse(surf2, black, (10/k, 0/k, 200/k, 90/k))
    surf3 = pygame.transform.rotate(surf1, 0)
    surf4 = pygame.transform.rotate(surf2, 60)
    surf3.blit(surf4, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    screen.blit(surf3,(x+130/k,y-160/k))
    polygon(screen, black, [(x+70/k,y+250/k), (x+170/k,y+20/k),
                              (x+170/k,y+190/k), (x+130/k,y+280/k),(x+70/k,y+300/k)]) 

def right_paw(x, y, k):
    '''
    Function draws panda's right paw
    '''
    surf1 = pygame.Surface((500/k, 500/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((500/k, 500/k), pygame.SRCALPHA)
    ellipse(surf1, black, (0/k, 0/k, 200/k, 400/k))
    ellipse(surf2, black, (120/k, 0/k, 200/k, 80/k))
    surf3 = pygame.transform.rotate(surf1, 20)
    surf4 = pygame.transform.rotate(surf2, 35)
    surf3.blit(surf4, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    screen.blit(surf3,(x-88/k,y+42/k))

def left_paw(x, y, k):
    '''
    Function draws panda's left paw
    '''    
    surf1 = pygame.Surface((700/k, 800/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((700/k, 800/k), pygame.SRCALPHA)
    ellipse(surf1, black, (0/k, 0/k, 200/k, 400/k))
    ellipse(surf2, black, (150/k, 480/k, 80/k, 200/k))
    surf3 = pygame.transform.rotate(surf1, 40)
    surf4 = pygame.transform.rotate(surf2, -10)
    surf3.blit(surf4, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    screen.blit(surf3,(x-200/k,y-450/k))
    polygon(screen, black, [(x+31/k,y+238/k), (x+65/k,y+210/k),
                                  (x+65/k,y+100/k)])

def head(x, y, k):
    '''
    Function draws panda's head
    '''
    surf1 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    ellipse(surf1, white, (0/k, 0/k, 210/k, 280/k))
    ellipse(surf2, white, (0/k, 70/k, 280/k, 210/k))
    surf1.blit(surf2, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    surf = pygame.transform.rotate(surf1,30)
    screen.blit(surf,(x-110/k, y-240/k))
    
def ears(x, y, k):   
    '''
    Function draws panda's ears
    '''    
    surf1 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    ellipse(surf1, black, (0/k, 0/k, 50/k, 100/k))
    ellipse(surf2, black, (10/k, 90/k, 50/k, 100/k))
    surf3 = pygame.transform.rotate(surf1,15)
    surf4 = pygame.transform.rotate(surf2, 0)
    surf3.blit(surf4, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    screen.blit(surf3,(x+120/k, y-120/k))
    surf1 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    surf2 = pygame.Surface((400/k, 500/k), pygame.SRCALPHA)
    ellipse(surf1, black, (0/k, 0/k, 50/k, 100/k))
    ellipse(surf2, black, (10/k, 90/k, 50/k, 100/k))
    surf3 = pygame.transform.rotate(surf1,15)
    surf4 = pygame.transform.rotate(surf2, 0)
    surf3.blit(surf4, (0, 0), special_flags = pygame.BLEND_RGBA_MIN)
    surf5 = pygame.transform.rotate(surf3, -60)
    screen.blit(surf5,(x-372/k, y-134/k))

def nose_and_eyes(x, y, k):
    '''
    Function draws panda's nose and eyes
    '''   
    ellipse(screen, black, (x+25/k, y+130/k, 60/k, 40/k))
    ellipse(screen, black, (x+70/k, y+50/k, 60/k, 60/k))
    ellipse(screen, black, (x-10/k, y+25/k, 50/k, 60/k))
    

#big bamboo
bamboo(400, 340, 1.8)
#panda baby
panda(320, 360, 2.6)
#panda
panda(460, 300, 1.8)
#small bamboo
bamboo(100, 350, 1.8)
bamboo(250, 410, 2.3)
bamboo(575, 300, 2.6)
                                    
#HERE WE GO
pygame.display.update()
clock = pygame.time.Clock()
finished = False
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
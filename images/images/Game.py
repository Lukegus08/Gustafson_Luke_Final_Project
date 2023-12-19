## This file was created by Luke Gustafson on 11/27/23
"sources"
''' 
Mr Cozart's class
tablemates colberation
class resorces
mkfeuhrer souce code from github 
https://www.sourcecodester.com/python/14565/air-hockey-game-using-python-source-code.html
http://kidscancode.org/blog/
'''
# goals 
'''
create a working air hockey game vs computer 
if posible create a multi player game with 2 people 
'''
"feture goals"
'''
add a timer feture with cirton amout of time for periods 
'''

import pygame
import time
from pygame.locals import *
import os

pygame.init()

# x = (800)
# y = (600)
# color is initalized 
white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
red = (255,0,0)
blue = (0,0,255)
light_blue = (147,251,253)

#Clock initialized
clock= pygame.time.Clock()
#Board Size
screen= pygame.display.set_mode((800,600))
#dividing line
divline1 = screen.get_width()/2, 0
divline2 = screen.get_width()/2 ,screen.get_height()
#Caption
pygame.display.set_caption('Air Hockey!')
#Font Sizes
smallfont = pygame.font.SysFont("comicsansms" , 25)
medfont = pygame.font.SysFont("comicsansms" , 45)
largefont = pygame.font.SysFont("comicsansms" , 65)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

#Create Game Objects(puck, goals, paddles)
goalheight = 50
goalwidth = 20
goal1 = pygame.Rect(0,screen.get_height()/2 - 50,10,100)
goal2 = pygame.Rect(screen.get_width()-10,screen.get_height()/2 - goalheight,10,100)
paddle1= pygame.Rect(screen.get_width()/2-200,screen.get_height()/2,20,20)
paddle2= pygame.Rect(screen.get_width()/2+200,screen.get_height()/2,20,20)
paddleVelocity= 4
Puck= pygame.Rect(screen.get_width()/2,screen.get_height()/2,20,20)
# pygame.draw.rect(red,[screen.get_width()/2,screen.get_height()/2,20,20])
divider= pygame.Rect(screen.get_width()/2,0,3,screen.get_height())
discVelocity= [5,5]
#  setup asset folders here - images sounds etc.
# import the images to the game 
disc = pygame.image.load(os.path.join(img_folder, 'disc.png'))
bluepadimg = pygame.image.load(os.path.join(img_folder, 'player.png'))
background = pygame.image.load(os.path.join(img_folder, 'airhockey.png'))
redpadimg = pygame.image.load(os.path.join(img_folder, 'comp.png'))

#Score
score1,score2 = 0,0
serveDirection=1
# the feture that resets the disc and allows it to set back to the center of i another team score sets to the other teams side 
def resetPuck():
    discVelocity[0]=5*serveDirection
    discVelocity[1]=5*serveDirection
    print(score1,score2)
    disc.x= screen.get_width()/2
    disc.y= screen.get_height()/2
# add text to the score of the game 
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text , True , color)
    elif size == "medium":
        textSurface = medfont.render(text , True , color)   
    elif size == "large":
        textSurface = largefont.render(text , True , color) 
    return textSurface , textSurface.get_rect()
# feture if the game is paused 
def pause():
    paused = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press c to continue , q to quit",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # gameDisplay.fill(white)
        clock.tick(5)    

def message_to_screen(msg,color,y_displace=0,x_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (screen.get_width()/2+x_displace) , ((screen.get_height()/2) + y_displace)
    screen.blit(textSurf,textRect)


def gameLoop():
    gameExit = False
    gameOver = False
    score2,score1=0,0
    while not gameExit:
        # hilight the event that taks place with the paddle 
        for event in pygame.event.get():
            down2,up2,up,down,left2,right2,right,left=0,0,0,0,0,0,0,0    # the position of the blue paddle          
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed() # keys that function the game (which is just the arrows on the bottom of the computer)
                if keys[K_LEFT]:
                    left = 1;
                elif keys[K_RIGHT]:
                    right = 1;
                elif keys[K_UP]:
                    up = 1;
                elif keys[K_DOWN]:
                    down = 1;
                elif keys[K_a]:
                    left2 = 1;
                elif keys[K_d]:
                    right2 = 1;    
                elif keys[K_w]:
                    up2 = 1;
                elif keys[K_s]:
                    down2 = 1; 
                elif keys[K_p]:
                    pause()             

        # pygame.draw.rect(gameDisplay,red,[randapplex,randappley,appleThickness,appleThickness])
        
        # gameDisplay.blit(discimg, 
        # (discx,discy)
        #Update Paddle1 (the set of of paddles an the reastio)
        paddle1.y+=(down2-up2)*paddleVelocity
        paddle1.x+=(right2-left2)*paddleVelocity
        if paddle1.y<5:
            paddle1.y=0
        elif paddle1.y>screen.get_height()-  paddle1.height:
            paddle1.y=screen.get_height()-  paddle1.height
        if paddle1.x<5:
            paddle1.x=0
        elif paddle1.x>screen.get_width()/2- paddle1.width:
            paddle1.x= screen.get_width()/2- paddle1.width

        #Update Paddle2
        paddle2.y+= (down-up)*paddleVelocity
        paddle2.x+= (right-left)*paddleVelocity
        if paddle2.y<0:
            paddle2.y=0
        elif paddle2.y>screen.get_height()-  paddle2.height:
            paddle2.y=screen.get_height()-  paddle2.height
        if paddle2.x>screen.get_width()- paddle1.width:
            paddle2.x= screen.get_width()- paddle1.width
        elif paddle2.x<screen.get_width()/2:
            paddle2.x= screen.get_width()/2

        #Update Puck(which allows the puck to deflect of of paddles, bundries, and a eventuly the puck falls in the bondy of the goal reset to the center line)
        Puck.x+=discVelocity[0]
        Puck.y+=discVelocity[1]
        if (Puck.x <= Puck.width and (Puck.y <= screen.get_height()/2 + goalheight) and (Puck.y >= screen.get_height() - goalheight)):
            score2+=1
            serveDirection=-1
            resetPuck()
        elif (Puck.x >= screen.get_width()-goalwidth-Puck.width) and (Puck.y <= screen.get_height()/2 + goalheight) and (Puck.y >= screen.get_height()/2 - goalheight):
            score1+=1
            serveDirection=1
            resetPuck()
        elif Puck.x - 10 < 0 or Puck.x + 25 > screen.get_width() :
            discVelocity[0]*=-1;    

        if Puck.y - 10 < 0  or Puck.y + 10 > screen.get_height() - Puck.height:
            discVelocity[1]*=-1
        if Puck.colliderect(paddle1) or Puck.colliderect(paddle2):
            discVelocity[0]*=-1


        #Render Logic(meaning that the movement of paddles and reaction to the disc interacting with the paddle)
        screen.fill(black)
        message_to_screen("Player 1",white,-250,-150,"small")
        message_to_screen(str(score1),white,-200,-150,"small")
        message_to_screen("Player 2",white,-250,150,"small")
        message_to_screen(str(score2),white,-200,150,"small")
        pygame.draw.rect(screen, (255,100, 100), paddle1)
        pygame.draw.rect(screen, (20,20,100), paddle2)  
        pygame.draw.rect(screen,light_blue,goal1)
        pygame.draw.rect(screen,light_blue,goal2)  
        screen.blit(disc,(Puck.x,Puck.y))   
        screen.blit(bluepadimg,(paddle1.x-5,paddle1.y-5))
        screen.blit(redpadimg,(paddle2.x-5,paddle2.y-5))
        # screen.blit(background,(100,100))
        pygame.draw.circle(screen, white ,(screen.get_width()/2, screen.get_height()/2), screen.get_width()/10,5)
        #boundaries and center line
        pygame.draw.line(screen , white , divline1, divline2 ,5 )
        pygame.draw.line(screen, blue,(0,0), (screen.get_width()/2 - 5,0) ,5)
        pygame.draw.line(screen, blue,(0,screen.get_height()), (screen.get_width()/2 - 5,screen.get_height()) ,5)
        pygame.draw.line(screen, red, (screen.get_width()/2+5,0), (screen.get_width() ,0) ,5)
        pygame.draw.line(screen, red, (screen.get_width()/2 + 5,screen.get_height()) , (screen.get_width(),screen.get_height()) ,5)
        pygame.draw.line(screen, blue, (0,0), (0,screen.get_height()/2-goalheight) ,5)
        pygame.draw.line(screen, blue, (0,screen.get_height()/2 + goalheight), (0,screen.get_height()) ,5)
        pygame.draw.line(screen, red, (screen.get_width(),0), (screen.get_width(),screen.get_height()/2-goalheight) ,5)
        pygame.draw.line(screen, red, (screen.get_width(),screen.get_height()/2 + goalheight), (screen.get_width(),screen.get_height()) ,5)
        # pygame.draw.circle(screen,red,(0,0))
        pygame.display.update()
        clock.tick(50)

gameLoop()  

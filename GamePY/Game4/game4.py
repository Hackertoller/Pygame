import pygame
import random
import sys
import time

rectX = 0
rectY = 500
bombX = rectX
bombY = rectY


red = (255,0,254)
blue = (0,255,255)
Yellow = (255, 255, 0)
black = (0,0,0)
EventKey = ''
Keys = ''
root = pygame.init()
Display = pygame.display.set_mode((1000,600))
ufoX = 960
ufoY = 0
animation = 2
font = pygame.font.Font(None,50)
score = 0
lives = 10
ufoSet = pygame.image.load('icons8-ufo-64.png')
UFOSET = pygame.transform.scale(ufoSet,(50,50))

pygame.mixer.music.load('world-m.ogg')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
def rect(rectX,rectY):
    Display.fill(black)
    SCORE = f'YOUR SCORE : {str(score)}'
    s = font.render(SCORE,True,Yellow)
    #---------------------------------
    LIVES = f'The number of spaceship lives : {str(lives)}'
    t = font.render(LIVES,True,(255,255,255))
    #---------------------------------
    Display.blit(s,(0,0))
    Display.blit(t,(400,0))
    Chars = pygame.image.load('Chars.png')
    CHARS = pygame.transform.scale(Chars,(50,50))
    Display.blit(CHARS,(rectX,rectY))
    
def bomb(bombX,bombY,EventKey):
    if EventKey == 'space':
        BombRect = pygame.draw.rect(Display,red,(bombX,bombY,30,10))


def ufo(ufoX,ufoY):
    Display.blit(UFOSET,(ufoX,ufoY))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                EventKey = 'space'
            elif event.key == pygame.K_UP:
                Keys = 'up'
            elif event.key == pygame.K_DOWN:
                Keys = 'down'
    for i in range(40):
        if ufoX == bombX and ufoY - i == bombY:
            try:
                score += 1
                lives -= 1
            except:
                sys.exit()
            if score == 10:
                score = 'You Win'
        elif ufoX == bombX and ufoY + i == bombY:
            try:
                score += 1
                lives -= 1
            except:
                sys.exit()
            if score == 10:
                score = 'You Win'
    
    ufoY += animation
    if ufoY > 600:
        animation = -2
    elif ufoY < 0:
        animation = 2
    if EventKey == 'space':
        bombX += 20
    if bombX > 1000:
        bombX = rectX
        bombY = rectY
        EventKey = ''
    if Keys == 'up':
        rectY -= 1
    elif Keys == 'down':
        rectY += 1
    if rectY > 600:
        rectY = 0
    elif rectY < 0:
        rectY = 600
    pygame.display.update()
    rect(rectX,rectY)
    bomb(bombX,bombY,EventKey)
    ufo(ufoX,ufoY)
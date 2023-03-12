import pygame
import sys
import random
import time
from pygame import mixer
mixer.init()

mixer.music.load('world-m.ogg')
mixer.music.play()
Blue = (0,255,255)
Red = (255,0,255)
color = Red
FlappyX = 90
FlappyY = 60
BlockX = 750
BlockY = 500
BlockHeight = 100
BlockHeight2 = 50
eventKey = ''

Help = 'Press Key Space'


root = pygame.init()
Display = pygame.display.set_mode((800,600))
flappy = pygame.image.load('Flappy.png')
FLAPPY = pygame.transform.scale(flappy,(50,50))

background = pygame.image.load('flappy-bird-background-png-2.png')
BACKGROUND = pygame.transform.scale(background,(800,600))
def Flappy(FlappyX,FlappyY,Help,color):
    Display.blit(BACKGROUND,(0,0))
    font = pygame.font.Font(None,50)
    help = font.render(Help,True,color)
    Display.blit(help,(0,0))
    if Help == 'You Crashed':
        time.sleep(2)
        sys.exit()
    else:
        #Display.fill((255,255,255))
        Display.blit(FLAPPY,(FlappyX,FlappyY))
def Block(BlockX,BlockY,BlockHeight,BlockHeight2):
    rect1 = pygame.draw.rect(Display,Blue,(BlockX,BlockY,50,BlockHeight))
    rect2 = pygame.draw.rect(Display,Red,(BlockX,0,50,BlockHeight2))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                FlappyY -= 110
    FlappyY +=4
    BlockX -= 3
    if BlockX < 0:
        BlockX = 750
        BlockHeight = random.randint(0,300)
        BlockY = 600 - BlockHeight
        BlockHeight2 = 600 - BlockHeight - 200
    for i in range(50):
        if FlappyY > BlockY and FlappyX + i == BlockX:
            Help = "You Crashed"
            color = Blue
            mixer.music.pause()
            mixer.music.load('lose-m.wav')
            mixer.music.play()
    for x in range(BlockHeight2):

        if FlappyX > BlockX and FlappyY - x == 0:
            Help = "You Crashed"
            color = Blue
            mixer.music.pause()
            mixer.music.load('lose-m.wav')
            mixer.music.play()
        
    Flappy(FlappyX,FlappyY,Help,color)
    Block(BlockX,BlockY,BlockHeight,BlockHeight2)
    pygame.display.update()
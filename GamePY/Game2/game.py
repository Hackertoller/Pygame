import pygame
import sys
import time
import random
# Width And Height For Games
width = 800
height = 600
Chars_X = 400
Chars_Y = 530
block_X = 400
block_Y = 0
# Colors
Black = (0,0,0)
red = (255,0,255)

#Events
EventChars = ''
# Charactors
root = pygame.init()

Display = pygame.display.set_mode((width,height))
Chars = pygame.image.load('Chars.png')

# functions
def CharsChange(Chars_X,Chars_Y):
    Display.fill(Black)
    text_X = "Press X To Left"
    text_Y = "Press Y To Right"
    font = pygame.font.Font(None,30)
    Help_X = font.render(text_X,True,red)
    Help_Y = font.render(text_Y,True,red)
    Display.blit(Help_X,(0,0)) 
    Display.blit(Help_Y,(600,0))
    CHARS = pygame.transform.scale(Chars,(50,50))
    Display.blit(CHARS,(Chars_X,Chars_Y))
def BlockChange(block_X,block_Y):
    rect = pygame.draw.rect(Display,red,(block_X,block_Y,50,50))
    pygame.display.flip()
    
    
def Colotion(block_X,block_Y,Chars_X,Chars_Y):
    for i in range(50):
        if block_Y + 100 == 600 and Chars_X + i == block_X:
            time.sleep(2)
            sys.exit()
        elif 600 - block_Y < 100 and Chars_X + i == block_X:
            time.sleep(2)
            sys.exit()
# Start Game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                EventChars = 'x'
            elif event.key == pygame.K_y:
                EventChars = 'y'
    block_Y += 3
    if EventChars == 'x':
        Chars_X += 1
        if Chars_X > 800:
            time.sleep(2)
            sys.exit()
    elif EventChars == 'y':
        Chars_X -= 1
        if Chars_X < 0:
            time.sleep(2)
            sys.exit()
    if block_Y > 600:
        block_Y = 0
        block_X = random.randrange(0,730)    
    CharsChange(Chars_X,Chars_Y)
    BlockChange(block_X,block_Y)
    Colotion(block_X,block_Y,Chars_X,Chars_Y)
    pygame.display.update()
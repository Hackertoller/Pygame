import pygame
import sys
import time
width = 1000
height = 600
Cat_X =  100
Cat_Y = 530
rect_X = 1000
rect_Y = 530
color = (0,0,0)
blue = (0,255,255)
white = (255,255,255)
score = 0


root = pygame.init()
game = pygame.display.set_mode((width,height))
font = pygame.font.Font(None, 50)


image = pygame.image.load('cat.png')
IMAGE = pygame.transform.scale(image,(70,70))
getfail = ''
time.sleep(5)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Cat_Y -= 200
    rect_X -= 5
    if rect_X == 0 and Cat_Y == 530:
        getfail = 'You Crashed'
    elif rect_X < 0 and Cat_Y < 530:
        score = score + 5
        time.sleep(0.2)
        rect_X = 1000
        time.sleep(0.4)
        Cat_Y = 530
    game.fill(white)
    text = f'Score : {str(score)}'
    SCORE = font.render(text , True, blue)
    failed = font.render(getfail,True,blue)
    game.blit(SCORE,(100,100))
    game.blit(IMAGE,(Cat_X,Cat_Y))
    game.blit(failed,(200,200))
    rect = pygame.draw.rect(game,blue,(rect_X,rect_Y,70,70))
    pygame.display.flip()
    if getfail == 'You Crashed':
        time.sleep(5)
        sys.exit()
    pygame.display.update()
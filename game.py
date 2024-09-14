import pygame
import time
pygame.init()
playing=True
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption('Happy Birthday')
img1=pygame.image.load('img1.jpg')
img2=pygame.image.load('img2.jpg')
img3=pygame.image.load('img3.jpg')

while playing:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            playing=False
    screen.blit(img1,(0,0))
    font=pygame.font.SysFont('Times New Roman',50)
    text=font.render('Happy Brithday',True,(15, 1, 1))
    screen.blit(text,(150,100))
    pygame.display.update()

    time.sleep(2)
    screen.blit(img2,(0,0))
    text2=font.render('I wish u a Happy Birthday ',True,(15,1,1))
    text3=font.render('and have a nice day:)',True,(15,1,1))
    screen.blit(text2,(90,150))
    screen.blit(text3,(120,200))
    pygame.display.update()
    time.sleep(2)
    
    
    screen.blit(img3,(0,0))
    font2=pygame.font.SysFont('Arial',50)
    text4=font2.render('See you again next year!',True,(15,1,1))
    screen.blit(text4,(100,80))
    pygame.display.update()    
    time.sleep(2)

  



    
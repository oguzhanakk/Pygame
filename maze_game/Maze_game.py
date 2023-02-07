import pygame
import sys
import time
import keyboard
from pygame import mixer

pygame.init()

#song
mixer.init()
mixer.music.load("mars.mp3")
sound_level = 1
mixer.music.set_volume(sound_level)
mixer.music.play()

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#playground setup
a=700
b=700
screen = pygame.display.set_mode((a, b))
pygame.display.set_caption("Maze game")
width = 20
length = 20
x = 20
y = 80
start_x = 20
start_y = 80
velocity = 10

#game creation
run = True
while run:
    pygame.time.delay(40)

    #to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #to create
    screen.fill((255, 255, 255)) #Background
    pygame.draw.circle(screen, (255, 255, 0), (x, y), (10)) #the ball

    #creating a maze
    #right
    pygame.draw.line(screen, black, (30, 50), (500, 50), 8)
    pygame.draw.line(screen, black, (30, 100), (450, 100), 8)
    if((x>=0 and x<=500) and y==50):
        #y += 10 the code in the comment line here is to prevent it from exiting the maze
        x = start_x
        y = start_y
    if((x>=0 and x<=450) and y==100):
        #y -= 10
        x = start_x
        y = start_y

    #down, big to the right
    pygame.draw.line(screen, black, (500, 50), (500, 200), 8)
    pygame.draw.line(screen, black, (450, 100), (450, 150), 8)
    if ((y>=50 and y<=200) and x == 500):
        #x -= 10
        x = start_x
        y = start_y
    if ((y>=100 and y<=150) and x == 450):
        #x += 10
        x = start_x
        y = start_y

    #left
    pygame.draw.line(screen, black, (500, 200), (80, 200), 8)
    pygame.draw.line(screen, black, (450, 150), (30, 150), 8)
    if ((x >= 80 and x <= 500) and y == 200):
        #y -= 10
        x = start_x
        y = start_y
    if ((x >= 30 and x <= 450) and y == 150):
        #y += 10
        x = start_x
        y = start_y

    #down, big left
    pygame.draw.line(screen, black, (80, 200), (80, 250), 8)
    pygame.draw.line(screen, black, (30, 150), (30, 300), 8)
    if ((y>=200 and y<=250) and x == 80):
        #x -= 10
        x = start_x
        y = start_y
    if ((y>=150 and y<=300) and x == 30):
        #x += 10
        x = start_x
        y = start_y

    #right
    pygame.draw.line(screen, black, (80, 250), (500, 250), 8)
    pygame.draw.line(screen, black, (30, 300), (450, 300), 8)
    if ((x >= 80 and x <= 500) and y == 250):
        #y += 10
        x = start_x
        y = start_y
    if ((x >= 30 and x <= 450) and y == 300):
        #y -= 10
        x = start_x
        y = start_y

    #down, big to the right
    pygame.draw.line(screen, black, (500, 250), (500, 400), 8)
    pygame.draw.line(screen, black, (450, 300), (450, 350), 8)
    if ((y>=250 and y<=400) and x == 500):
        #x -= 10
        x = start_x
        y = start_y
    if ((y>=300 and y<=350) and x == 450):
        #x += 10
        x = start_x
        y = start_y

    #left
    pygame.draw.line(screen, black, (500, 400), (70, 400), 8)
    pygame.draw.line(screen, black, (450, 350), (30, 350), 8)
    if ((x >= 70 and x <= 500) and y == 400):
        #y -= 10
        x = start_x
        y = start_y
    if ((x >= 30 and x <= 450) and y == 350):
        #y += 10
        x = start_x
        y = start_y

    #down, big left
    pygame.draw.line(screen, black, (70, 400), (70, 450), 8)
    pygame.draw.line(screen, black, (30, 350), (30, 500), 8)
    if ((y>=400 and y<=450) and x == 70):
        #x -= 10
        x = start_x
        y = start_y
    if ((y>=350 and y<=500) and x == 30):
        #x += 10
        x = start_x
        y = start_y

    #right
    pygame.draw.line(screen, black, (70, 450), (350, 450), 8)
    pygame.draw.line(screen, black, (30, 500), (350, 500), 8)
    if ((x >= 70 and x <= 350) and y == 450):
        #y += 10
        x = start_x
        y = start_y
    if ((x >= 30 and x <= 350) and y == 500):
        #y -= 10
        x = start_x
        y = start_y

    #end button
    fontt = pygame.font.SysFont('Arial', 25)
    article = fontt.render('Finish', True, white)
    article2 = fontt.render('Press space', True, black)

                            #button color, position, length(x),width(y)
    pygame.draw.rect(screen, (130, 130, 130), (400, 450, 70, 40))
    screen.blit(article, (400, 450)) #text-> information, location

    #change when pressing the button
    if ((x >=410 and x <= 470) and (y >= 450 and y <= 490)):
        pygame.draw.rect(screen, (210, 210, 210), (400, 450, 70, 40))
        screen.blit(article2, (400, 450))


    #to move
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x>0:
        x -= velocity
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y<b-length:
        y += velocity
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x<a-width:
        x += velocity
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and y>0:
        y -= velocity
    if (keys[pygame.K_SPACE]):
        time.sleep(2)
        keyboard.press("space")
        image = pygame.image.load("korkunc.jpg").convert()
        image_location = screen.blit(image, (50, 50))
        mixer.music.load("korkunc.mp3")
        mixer.music.play()
    if (keys[pygame.K_ESCAPE]):
        break

    pygame.display.flip()

pygame.quit()
import pygame
import sys
import random
from pygame import mixer

#song
mixer.init()
mixer.music.load("valse.mp3")
ses_seviye = 1
mixer.music.set_volume(ses_seviye)
mixer.music.play()

#colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

#playground
a = 600 #x width
b = 600 #y height

#game velocity
FPS = 50
fpsClock = pygame.time.Clock()

#ball informations
x_Pos_circle = a-(a/2)
y_Pos_circle = b-(b/2)
x_Vel_circle = 5 #Velocity
y_Vel_circle = 5 #Velocity
cap = 10

#square box information
x_Pos_line = a-200
y_Pos_line = b-35
x_Vel_line = 10 #Velocity
en = 70
boy = 15

#playground setup
pygame.init()
screen = pygame.display.set_mode((a, b))
pygame.display.set_caption("Ping-Pong game")

#text information at the end of the gamei
font = pygame.font.SysFont('Timesnewroman', 50)
text = font.render('Elendiniz..', True, red, (0, 0, 0))
text_box = text.get_rect()
text_box.center = ((a // 2), (b // 2))

#location - size of the boxes in the game
width_box = 40
height_box = 40
box_x = []
box_y = []
for i in range(0,30):
    box_xrandom = random.randint(0, a - 40)
    #to make the number a multiple of 5, because the speed of the ball is 5
    kutu_xrandom_temporary = box_xrandom % 5
    box_xrandom -= kutu_xrandom_temporary

    box_yrandom = random.randint(0, b - 150)
    #to make the number a multiple of 5, because the speed of the ball is 5
    kutu_y_random_temporary = box_yrandom % 5
    box_yrandom -= kutu_y_random_temporary

    #son cikan kare bir önceki kare ile cakisiyosa o kareyi olusturmuyor.
    #ama sorun bir önceki kare degil butun kareler ile kiyaslaman lazim.
    #140                #100,180
    if (i != 0 and i != 1):
        if ((box_xrandom > (box_x[len(box_x) - 1] - 40)) and (box_xrandom < (box_x[len(box_x) - 1] + 40))):
            continue

    # 140                #100,180
    if (i != 0 and i != 1):
        if ((box_yrandom > (box_y[len(box_y) - 1] - 40)) and (box_yrandom < (box_y[len(box_y) - 1] + 40))):
            continue

    box_x.append(box_xrandom)
    box_y.append(box_yrandom)

#game start loop
start = True
while start:
    #background color
    screen.fill(black)

    #main objects in the game
    pygame.draw.rect(screen, green, (x_Pos_line, y_Pos_line, en, boy)) #the box we play
    pygame.draw.circle(screen, green, (x_Pos_circle, y_Pos_circle), cap, 0) #ball

    #boxes in the game
    for i in range(0, len(box_x)):
        pygame.draw.rect(screen, red, (box_x[i], box_y[i], width_box, height_box))

    #to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            start = False
            sys.exit()

    #ball movement
    x_Pos_circle -= x_Vel_circle
    y_Pos_circle -= y_Vel_circle

    #out-of-bounds ping-pong effect
        #right-left collision
    if x_Pos_circle > a-cap or x_Pos_circle < cap:
        x_Vel_circle *= -1
        #up collision
    if y_Pos_circle < cap:
        y_Vel_circle *= -1

    #the game is over. printing
    if y_Pos_circle > b:
        screen.blit(text, text_box)

    #bouncing the ball off the line.
    if  ((x_Pos_circle >= x_Pos_line-boy and x_Pos_circle <= x_Pos_line+en) and y_Pos_circle == y_Pos_line):
        y_Vel_circle *= -1

    #if it hits the box, the box disappears
    for i in range(0, len(box_x)):
        #hitting the left or right of the box
        if (((y_Pos_circle > box_y[i] and y_Pos_circle < box_y[i] + 60) and x_Pos_circle == box_x[i]) or ((y_Pos_circle > box_y[i] and y_Pos_circle < box_y[i] + 50) and x_Pos_circle == box_x[i] + 60)):
            #the reflection is in the reverse right-left direction
            x_Vel_circle *= -1
            #destroy the box
            box_x[i] = 1000
            box_y[i] = 1000

        #hitting the top or bottom of the box
        if (((x_Pos_circle > box_x[i] and x_Pos_circle < box_x[i] + 50) and y_Pos_circle == box_y[i]) or ((x_Pos_circle > box_x[i] and x_Pos_circle < box_x[i] + 50) and y_Pos_circle == box_y[i] + 60)):
            #mirroring in reverse top-bottom direction
            y_Vel_circle *= -1
            #destroy the box
            box_x[i] = 1000
            box_y[i] = 1000

    #move the line left and right
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x_Pos_line > 0:
        x_Pos_line -= x_Vel_line
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x_Pos_line < a-en:
        x_Pos_line += x_Vel_line

    pygame.display.flip()
    fpsClock.tick(FPS)

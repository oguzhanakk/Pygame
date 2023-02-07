import pygame
import sys
import random

#playground setup
pygame.init()
a = 500
b = 500
screen = pygame.display.set_mode((a, b))
pygame.display.set_caption("gold collecting game")

#colors
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#Money informations
class Money:
    def __init__(self):
        self.x = random.randint(0, a)
        self.y = random.randint(0, b)
        self.gather = False

    def draw(self):
        pygame.draw.circle(screen, yellow, (self.x, self.y), 5)

#Player informations
class Player:
    def __init__(self):
        self.x = a/2
        self.y = b/2
        self.vel = 0.1  #velocity
        self.point = 0

    def draw(self):
        pygame.draw.rect(screen, blue, (self.x, self.y, 20, 20))

#Score informations
class Score:
    def __init__(self, x, en):
        self.x = x
        self.en = en
        self.article = ""


    def update(self, score):
        font = pygame.font.SysFont('Arial', 10)
        self.text = str(score)
        pygame.draw.rect(screen, red, (self.x, 5, self.en, 12))
        text = font.render(self.text, 1, white)
        screen.blit(text, (self.x + (self.en / 2 - text.get_width() / 2), 5 + (12 / 2 - text.get_height() / 2)))

#assign to class
o = Player()
moneys = []
points = Score(5, 15)

#create money circles
for i in range(15):
    p = Money()
    moneys.append(p)

#refresh function
def refresh():
    screen.fill(black)
    o.draw()
    for p in moneys:
        if p.gather == False:
            p.draw()

    points.update(o.point)
    pygame.display.update()

#game creation
start = True
while start:
    refresh()
    #Close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
            break

    #move with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w] and o.y>0:
        o.y -= o.vel
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and o.y<b-20:
        o.y += o.vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and o.x<a-20:
        o.x += o.vel
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and o.x>0:
        o.x -= o.vel

    #money circles disappear if you take the money
    for p in moneys:
        if p.x >= o.x and p.x <= (o.x + 20) and p.y >= o.y  and p.y <= (o.y + 20):
            o.point += 1
            p.gather = True
            moneys.remove(p)
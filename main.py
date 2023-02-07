import pygame
import random
import os
import time
from Pictures_info import *
from Functions import *

pygame.init()
pygame.font.init()

# Main menu


def Menu():
    title_font = pygame.font.SysFont("Arial", 45)
    start = True
    # Game loop
    while start:
        screen.blit(background_picture, (0, 0))
        title_text = title_font.render("Click to start the game..", 1, (255, 0, 0))
        screen.blit(title_text, (width / 2 - title_text.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Start_game()
    pygame.quit()


Menu()

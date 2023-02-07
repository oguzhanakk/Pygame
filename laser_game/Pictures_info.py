import pygame

# Game map information
width, height = 750, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Laser game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Plane pictures
blue_plane = pygame.image.load("./pictures/pixel_ship_blue_small.png")
green_plane = pygame.image.load("./pictures/pixel_ship_green_small.png")
red_plane = pygame.image.load("./pictures/pixel_ship_red_small.png")
yellow_plane = pygame.image.load("./pictures/pixel_ship_yellow.png")
# Laser pictures
blue_laser = pygame.image.load("./pictures/pixel_laser_blue.png")
green_laser = pygame.image.load("./pictures/pixel_laser_green.png")
red_laser = pygame.image.load("./pictures/pixel_laser_red.png")
yellow_laser = pygame.image.load("./pictures/pixel_laser_yellow.png")
# Background picture
background_picture = pygame.image.load("./pictures/background.jpeg")
BG = pygame.transform.scale(background_picture, (width, height)) #We're compressing it because the background image is too big.

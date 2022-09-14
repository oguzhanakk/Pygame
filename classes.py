import pygame
from Pictures_info import *

# Classes = Laser , plane , enemy, player

# Collision status
def collision(obj1, obj2):
    diff_x = obj2.x - obj1.x
    diff_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (diff_x, diff_y)) != None

# Laser class
class LaserInformation:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        #pygame function to fix the picture
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, acceleration):
        self.y += acceleration

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, object):
        return collision(self, object)

# Plane class
# Main class information
class Plane:
    FILLING = 30
    def __init__(self, x, y, life=100):
        self.x = x
        self.y = y
        self.life = life
        self.plane_picture = None
        self.laser_picture = None
        self.lasers = []
        self.laser_time = 0

    # To draw the plane
    def draw(self, screen):
        screen.blit(self.plane_picture, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(screen)

    def fill_time(self):
        if self.laser_time >= self.FILLING:
            self.laser_time = 0
        elif self.laser_time > 0:
            self.laser_time += 1

    def laser_movement(self, acceleration, objective):
        self.fill_time()
        for laser in self.lasers:
            laser.move(acceleration)
            if laser.off_screen(height):
                self.lasers.remove(laser)
            elif laser.collision(objective):
                objective.life -= 10
                self.lasers.remove(laser)

    def fire(self):
        if self.laser_time == 0:
            laser = LaserInformation(self.x, self.y, self.laser_picture)
            self.lasers.append(laser)
            self.laser_time = 1

    def height_information(self):
        return self.plane_picture.get_height()

    def width_information(self):
        return self.plane_picture.get_width()

# Private plane, enemy plane information
class Enemy(Plane):
    enemy_list = {"red": (red_plane, red_laser),
                       "blue": (blue_plane, blue_laser),
                       "green": (green_plane, green_laser)}

    def __init__(self, x, y, colour, life=100):
        super().__init__(x, y, life)
        self.plane_picture, self.laser_picture = self.enemy_list[colour]
        self.mask = pygame.mask.from_surface(self.plane_picture)

    def move(self, acceleration):
        self.y += acceleration

    def fire(self):
        if self.laser_time == 0:
            laser = LaserInformation(self.x, self.y + 20, self.laser_picture)
            self.lasers.append(laser)
            self.laser_time = 1

# Private plane , Player plane information
class Player(Plane):
    def __init__(self, x, y, life=100):
        super().__init__(x, y, life)
        self.plane_picture = yellow_plane
        self.laser_picture = yellow_laser
        self.mask = pygame.mask.from_surface(self.plane_picture)
        self.max_life = life

    def laser_movement(self, acceleration, objectivee):
        self.fill_time()
        for laser in self.lasers:
            laser.move(acceleration)
            if laser.off_screen(height):
                self.lasers.remove(laser)
            else:
                for obj in objectivee:
                    if laser.collision(obj):
                        objectivee.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, screen):
        super().draw(screen)
        self.life_bar(screen)

    def life_bar(self, screen):
        pygame.draw.rect(screen, red, (self.x, self.y + self.plane_picture.get_height() + 10, self.plane_picture.get_width(), 10))
        pygame.draw.rect(screen, green, (self.x, self.y + self.plane_picture.get_height() + 10, self.plane_picture.get_width() * (self.life / self.max_life), 10))

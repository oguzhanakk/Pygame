import pygame
import random
from classes import *
from Pictures_info import *

def Start_game():
    # Initial conditions
    start = True
    FPS = 60
    level = 0
    life = 5
    main_font = pygame.font.SysFont("Arial", 50)
    lose_font = pygame.font.SysFont("Arial", 90)
    enemys = []
    wave = 3
    enemy_acceleration = 1
    player_acceleration = 5
    laser_acceleration = 5
    player = Player(350, 650)
    clock = pygame.time.Clock()
    lose = False
    lose_counter = 0

    def create_screen():
        screen.blit(background_picture, (0, 0))
        # Articles
        life_text = main_font.render(f"Life : {life}", 1, white)
        chapter_text = main_font.render(f"Section: {level}", 1, white)
        screen.blit(life_text, (10, 10))
        screen.blit(chapter_text, (width - chapter_text.get_width() - 10, 10))

        for enemy in enemys:
            enemy.draw(screen)

        player.draw(screen)

        # Death text
        if lose:
            lose_write = lose_font.render("Game Over!", 1, white)
            screen.blit(lose_write, (width / 2 - lose_write.get_width()/2, height / 2 - lose_write.get_height()))

        pygame.display.update()

    while start:
        clock.tick(FPS)
        create_screen()

        # Condition of death
        if life <= 0 or player.life <= 0:
            lose = True
            lose_counter += 1

        if lose:
            if lose_counter > FPS * 3:
                start = False
            else:
                continue

        # Level up when the enemy is over
        if len(enemys) == 0:
            level += 1
            wave += 3

            for i in range(wave):
                # Enemy planes landing places, random.randrange = random number                  #random selection
                enemy = Enemy(random.randrange(50, width - 50), random.randrange(-1000, -100), random.choice(["red", "blue", "green"]))
                enemys.append(enemy)

        # Close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Give direction with keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_acceleration > 0:
            player.x -= player_acceleration
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x - player_acceleration < width:
            player.x += player_acceleration
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_acceleration > 0:
            player.y -= player_acceleration
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y - player_acceleration < height:
            player.y += player_acceleration
        if keys[pygame.K_SPACE]:
            player.fire()

        # Enemy move
        for enemy in enemys[:]:
            enemy.move(enemy_acceleration)
            enemy.laser_movement(laser_acceleration, player)

            # The time when the enemy fires
            if random.randrange(0, 120) == 1:
                enemy.fire()

            # Clash with the enemy
            if collision(enemy, player):
                player.life -= 10
                enemys.remove(enemy)
            # If the enemy crosses the bottom of the map
            elif enemy.y + enemy.height_information() > height:
                life -= 1
                enemys.remove(enemy)

        player.laser_movement(-laser_acceleration, enemys)
import pygame
import os
import math
from ship import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

lasers = []
laserSpeed = 10


script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

ship = PlayerShip(Pos(100, 100), 5, os.path.join(images_dir, 'ship.png'), screen)
e1ship = EnemyShip(Pos(100, 300), 3, os.path.join(images_dir, 'enemy.png'), screen)


# Load the bullet image
# bullet_path = os.path.join(images_dir, 'bullet.png')
# bulletImage = pygame.image.load(bullet_path)

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         radians = math.radians(angle)
        #         laser_dx = math.cos(radians) * laserSpeed
        #         laser_dy = -math.sin(radians) * laserSpeed
        #         lasers.append({'pos': [shipPos[0] + 25, shipPos[1] + 25], 'dir': (laser_dx, laser_dy), 'angle': angle})

    # Update position
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    ship.eval_input(keys, mouse_pos)
    ship.move()

    e1ship.generateMove()
    e1ship.move()

    screen.fill(pygame.Color(20, 23, 36))

    ship.draw()
    e1ship.draw()

    # Update lasers
    # for laser in lasers[:]:
    #     x, y = laser['pos'][0], laser['pos'][1]
    #     rotated_bullet = pygame.transform.rotate(bulletImage, laser['angle'])
    #     new_rect = rotated_bullet.get_rect(center=(x, y))
    #     screen.blit(rotated_bullet, new_rect.topleft)
    #     laser['pos'][0] += laser['dir'][0]
    #     laser['pos'][1] += laser['dir'][1]
    #     sx, sy = pygame.display.get_window_size()
    #     if x < -5 or y < -5 or x > sx+5 or y > sy+5:
    #         lasers.remove(laser)



    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()

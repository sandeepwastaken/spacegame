import pygame
import os
import math
import ship

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
shipPos = [100, 100]
triangleSpeed = 5
lasers = []
laserSpeed = 10
shipAngle = 0
angle = 0
shipMoveDir = None

def blurPos(topleft, amount, shipMoveDir):
    bx, by = topleft
    if shipMoveDir == "UP":
        by += amount
    elif shipMoveDir == "DOWN":
        by -= amount
    elif shipMoveDir == "RIGHT":
        bx -= amount
    elif shipMoveDir == "LEFT":
        bx += amount
    return (bx, by)

script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# Load and scale the spaceship image
ship_path = os.path.join(images_dir, 'ship.png')
shipImage = pygame.image.load(ship_path)
shipImage = pygame.transform.scale(shipImage, (50, 50))  # Resize for better rotation
shipOrig = shipImage.copy()  # Keep original image for rotation

# Load the bullet image
bullet_path = os.path.join(images_dir, 'bullet.png')
bulletImage = pygame.image.load(bullet_path)

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                radians = math.radians(angle)
                laser_dx = math.cos(radians) * laserSpeed
                laser_dy = -math.sin(radians) * laserSpeed
                lasers.append({'pos': [shipPos[0] + 25, shipPos[1] + 25], 'dir': (laser_dx, laser_dy), 'angle': angle})

    # Update position
    shipMoveDir = None
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        shipPos[0] -= triangleSpeed
        shipMoveDir = "LEFT"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        shipPos[0] += triangleSpeed
        shipMoveDir = "RIGHT"
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        shipPos[1] -= triangleSpeed
        shipMoveDir = "UP"
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        shipPos[1] += triangleSpeed
        shipMoveDir = "DOWN"

    # Get mouse position and calculate angle
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx, dy = mouse_x - (shipPos[0] + 25), mouse_y - (shipPos[1] + 25)
    desiredAngle = math.degrees(math.atan2(-dy, dx)) 
    angleDiff = (desiredAngle - angle + 180) % 360 - 180
    angle += angleDiff / 10

    # Clear screen
    screen.fill(pygame.Color(20, 23, 36))

    # Update lasers
    for laser in lasers[:]:
        x, y = laser['pos'][0], laser['pos'][1]
        rotated_bullet = pygame.transform.rotate(bulletImage, laser['angle'])
        new_rect = rotated_bullet.get_rect(center=(x, y))
        screen.blit(rotated_bullet, new_rect.topleft)
        laser['pos'][0] += laser['dir'][0]
        laser['pos'][1] += laser['dir'][1]
        sx, sy = pygame.display.get_window_size()
        if x < -5 or y < -5 or x > sx+5 or y > sy+5:
            lasers.remove(laser)

    rotated_ship = pygame.transform.rotate(shipOrig, angle)
    new_rect = rotated_ship.get_rect(center=(shipPos[0] + 25, shipPos[1] + 25))
    rotated_ship.set_alpha(64)
    screen.blit(rotated_ship, blurPos(new_rect.topleft, 12, shipMoveDir))
    rotated_ship.set_alpha(128)
    screen.blit(rotated_ship, blurPos(new_rect.topleft, 6, shipMoveDir))
    rotated_ship.set_alpha(255)
    screen.blit(rotated_ship, new_rect.topleft)


    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
import math
import pygame as pygame
import os as os
from enum import Enum
from laser import Laser
import copy

script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

class Pos:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

class Ship:
    def __init__(self, pos:Pos, speed:int, asset_path:str, screen, laser:Laser):
        self.size = 100
        self.pos:Pos = pos
        self.speed:int = speed
        self.texture = pygame.image.load(os.path.join(images_dir, asset_path)) 
        self.texture_size = (self.size, self.texture.get_height()/(self.texture.get_width()/self.size))
        self.texture = pygame.transform.scale(self.texture, self.texture_size)
        self.angle:float = 0
        self.moveDirection:Direction = Direction.NONE
        self.screen = screen
        self.laser:Laser = laser

    def fire(self):
        self.laser.fire(copy.deepcopy(self.pos), self.angle)

    def move(self):
        if self.moveDirection == Direction.LEFT:
            self.pos.x -= self.speed
        if self.moveDirection == Direction.RIGHT:
            self.pos.x += self.speed
        if self.moveDirection == Direction.UP:
            self.pos.y -= self.speed
        if self.moveDirection == Direction.DOWN:
            self.pos.y += self.speed

    def touchingWall(self):
        walls = []
        window = self.screen.get_rect()
        if self.pos.x <= 0:
            walls.append(Direction.LEFT)
        if self.pos.y <= 0:
            walls.append(Direction.UP)
        if self.pos.x >= window.width:
            walls.append(Direction.RIGHT)
        if self.pos.y >= window.height:
            walls.append(Direction.DOWN)

        return walls

    def draw(self):
        self.laser.move_and_draw(self.screen)

        def blurPos(topleft, amount):
            bx, by = topleft
            if self.moveDirection == "UP":
                by += amount
            elif self.moveDirection == "DOWN":
                by -= amount
            elif self.moveDirection == "RIGHT":
                bx -= amount
            elif self.moveDirection == "LEFT":
                bx += amount
            return (bx, by)

        rotated_ship = pygame.transform.rotate(self.texture, self.angle)
        new_rect = rotated_ship.get_rect(center=(self.pos.x, self.pos.y))
        rotated_ship.set_alpha(64)
        self.screen.blit(rotated_ship, blurPos(new_rect.topleft, 12))
        rotated_ship.set_alpha(128)
        self.screen.blit(rotated_ship, blurPos(new_rect.topleft, 6))
        rotated_ship.set_alpha(255)
        self.screen.blit(rotated_ship, new_rect.topleft)

class PlayerShip(Ship):
    def __init__(self, pos:Pos, speed:int, asset_path:str, screen, laser:Laser):
        super().__init__(pos, speed, asset_path, screen, laser)

    def eval_input(self, key, mouse):
        self.moveDirection = Direction.NONE
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.pos.x -= self.speed
            self.moveDirection = Direction.LEFT
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.pos.x += self.speed
            self.moveDirection = Direction.RIGHT
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.pos.y -= self.speed
            self.moveDirection = Direction.UP
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.pos.y += self.speed
            self.moveDirection = Direction.DOWN

        mouse_x, mouse_y = mouse
        dx, dy = mouse_x - (self.pos.x), mouse_y - (self.pos.y)
        desiredAngle = math.degrees(math.atan2(-dy, dx)) 
        angleDiff = (desiredAngle - self.angle + 180) % 360 - 180
        self.angle += angleDiff / 10


class EnemyShip(Ship):
    def __init__(self, pos:Pos, speed:int, asset_path:str, screen, laser:Laser):
        super().__init__(pos, speed, asset_path, screen, laser)
        self.moveDirection = Direction.RIGHT

    def generateMove(self):
        walls = self.touchingWall()
        if Direction.RIGHT in walls:
            self.moveDirection = Direction.LEFT
        if Direction.LEFT in walls:
            self.moveDirection = Direction.RIGHT


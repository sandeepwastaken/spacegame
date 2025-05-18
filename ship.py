import math
import pygame as pygame
import os as os
from enum import Enum

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
    def __init__(self, pos:Pos, speed:int, asset_path:str):
        self.pos:Pos = pos
        self.speed:int = speed
        self.texture = pygame.image.load(os.path.join(images_dir, asset_path)) 
        self.texture = pygame.transform.scale(self.texture, (50, 50))
        self.angle:float = 0
        self.moveDirection:Direction = Direction.NONE

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
        dx, dy = mouse_x - (self.pos.x + 25), mouse_y - (self.pos.y + 25)
        desiredAngle = math.degrees(math.atan2(-dy, dx)) 
        angleDiff = (desiredAngle - self.angle + 180) % 360 - 180
        self.angle += angleDiff / 10

    def move(self):
        if self.moveDirection == Direction.LEFT:
            self.pos.x -= self.speed
        if self.moveDirection == Direction.RIGHT:
            self.pos.x += self.speed
        if self.moveDirection == Direction.UP:
            self.pos.y -= self.speed
        if self.moveDirection == Direction.DOWN:
            self.pos.y += self.speed


    def draw(self, screen):
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
        new_rect = rotated_ship.get_rect(center=(self.pos.x + 25, self.pos.y + 25))
        rotated_ship.set_alpha(64)
        screen.blit(rotated_ship, blurPos(new_rect.topleft, 12))
        rotated_ship.set_alpha(128)
        screen.blit(rotated_ship, blurPos(new_rect.topleft, 6))
        rotated_ship.set_alpha(255)
        screen.blit(rotated_ship, new_rect.topleft)





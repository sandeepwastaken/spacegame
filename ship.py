import math as m
import pygame as pygame
import os as os

script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

class Pos:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class Ship:
    def __init__(self, pos:Pos, speed:int, asset_path:str):
        self.pos:Pos = pos
        self.speed:int = speed
        self.texture = pygame.image.load(os.path.join(images_dir, asset_path)) 
        self.texture = pygame.transform.scale(shipImage, (50, 50))
        self.angle:float = 0
        self.moveDirection = None
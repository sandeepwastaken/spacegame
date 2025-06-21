import pygame
import math

class Laser:
	def __init__(self, speed, asset_path):
		self.lasers = []
		self.speed = speed
		self.texture = pygame.image.load(asset_path)

	def fire(self, pos, angle):
		radians = math.radians(angle)
		laser_dx = math.cos(radians) * self.speed
		laser_dy = -math.sin(radians) * self.speed
		self.lasers.append({'pos': pos, 'dir': (laser_dx, laser_dy), 'angle': angle})

	def move_and_draw(self, screen):
		for laser in self.lasers[:]:
			x, y = laser['pos'].x, laser['pos'].y
			rotated_bullet = pygame.transform.rotate(self.texture, laser['angle'])
			new_rect = rotated_bullet.get_rect(center=(x, y))
			laser['pos'].x += laser['dir'][0]
			laser['pos'].y += laser['dir'][1]
			sx, sy = pygame.display.get_window_size()
			if x < -5 or y < -5 or x > sx+5 or y > sy+5:
				self.lasers.remove(laser)
			screen.blit(rotated_bullet, new_rect.topleft)

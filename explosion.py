import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):

	def __init__(self, object):
	
		super(Explosion, self).__init__()
		self.screen = object.screen
		settings = object.ai_settings
		self.image = pygame.image.load('Assets/PNG/Lasers/laserRed08.PNG')
		self.rect = (object.rect.top, object.rect.left, 0, 0)
		print(self.rect)
		self.rect.centerx = object.centerX
		self.rect.centery = object.centerY
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
		self.time = settings.explosionTime
		self.growth = settings.explosionSize / self.time

	def update(self):
		self.centy -= self.speed_factor
		self.rect.y = self.y
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
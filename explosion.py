import pygame
import copy

class Explosion():

	def __init__(self, object):
	
		super(Explosion, self).__init__()
		self.screen = object.screen
		settings = object.ai_settings
		self.image = pygame.image.load('Assets/PNG/Lasers/laserRed08.PNG')
		self.rect = copy.deepcopy(object.rect)
		self.rect.width = 0
		self.rect.height = 0
		
		self.centerx = object.centerX
		self.centery = object.centerY
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery 
		
		self.time = settings.explosionTime
		self.finalSize = object.rect.width
		self.growth = self.finalSize / self.time
		 
		
	def update(self):
		if (self.rect.width > self.finalSize):
			self.rect.width += self.growth
			self.rect.height += self.growth
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
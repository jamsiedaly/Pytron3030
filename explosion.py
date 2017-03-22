import pygame
import copy

class Explosion():

	def __init__(self, parent):
	
		super(Explosion, self).__init__()
		self.screen = parent.screen
		settings = parent.ai_settings
		self.image = pygame.image.load('Assets/PNG/Lasers/laserRed08.PNG')
		self.rect = copy.deepcopy(parent.rect)
		self.rect.width = 0
		self.rect.height = 0
		
		self.centerx = parent.centerX
		self.centery = parent.centerY
		
		self.rect.centerx = self.centerx[0]
		self.rect.centery = self.centery[0]
		
		self.time = settings.explosionTime
		self.finalSize = parent.rect.width * 2
		self.growth = self.finalSize / self.time
		 
		
	def update(self):
		if (self.rect.width < self.finalSize):
			self.rect.width += self.growth
			self.rect.height += self.growth
			return True
		else:
			return False
		
	def blitme(self):
		#self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		self.screen.blit(self.image, self.rect)
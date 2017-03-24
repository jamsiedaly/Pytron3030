import pygame
import copy
import random
from random import randint

class Explosion():

	def __init__(self, parent):
	
		super(Explosion, self).__init__()
		self.screen = parent.screen
		settings = parent.ai_settings
		animation1 = randint(1,3)
		animation2 = randint(1,3)
		explosionAnimation = 'Assets/PNG/Damage/playerShip'+ str(animation1) +'_Damage'+ str(animation2) +'.PNG'
		self.image = pygame.image.load(explosionAnimation)
		self.rect = copy.deepcopy(parent.rect)
		self.rect.width = 0
		self.rect.height = 0
		
		self.centerX = parent.centerX 
		self.centerY = parent.centerY
		
		self.rect.centerx = self.centerX[0]
		self.rect.centery = self.centerY[0]
		
		self.time = settings.explosionTime
		self.finalSize = parent.rect.width * 2
		self.growth = self.finalSize / self.time
		self.rotate = random.uniform(-2, 2)
		 
		
	def update(self):
		if (self.rect.width < self.finalSize):
			self.rect.width += self.growth
			self.rect.height += self.growth
			self.rect.centerx -= self.growth/2
			self.rect.centery -= self.growth/2
			self.image = pygame.transform.rotate(self.image, self.rotate)
			self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
			return True
		else:
			return False
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
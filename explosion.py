import pygame
import copy
import random
from random import randint

class Explosion():

	def __init__(self, parent):
	
		super(Explosion, self).__init__()
		self.screen = parent.screen
		self.settings = parent.ai_settings
		animation1 = randint(1,3)
		animation2 = randint(1,3)
		explosionAnimation = 'Assets/PNG/Damage/playerShip'+ str(animation1) +'_Damage'+ str(animation2) +'.PNG'
		self.image = pygame.image.load(explosionAnimation)
		self.rect = copy.deepcopy(parent.rect)
		self.rect.width = 0
		self.rect.height = 0
		
		self.rect.centerx = parent.rect.x + parent.rect.width/2
		self.rect.centery = parent.rect.y + parent.rect.height/2
		
		self.time = self.settings.explosionTime
		self.finalSize = parent.rect.width * 2
		self.growth = self.finalSize / self.time
		self.rotate = random.uniform(-3.5, 3.5)
		 
	def erase(self):
		pygame.draw.rect(self.screen,self.settings.bg_color, self.rect)
		
	def blitme(self):
		if (self.rect.width < self.finalSize):
			self.rect.width += self.growth
			self.rect.height += self.growth
			self.rect.centerx -= self.growth/2
			self.rect.centery -= self.growth/2
			self.image = pygame.transform.rotate(self.image, self.rotate)
			self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
			self.screen.blit(self.image, self.rect)
			return True
		else:
			return False
		
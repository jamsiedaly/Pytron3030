import pygame
from random import randint
from pygame.sprite import Sprite
from hitbox import Hitbox

class Alien :
	 
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('Assets/BitmapV/Enemy.bmp')
		self.rect = self.image.get_rect()
		self.speed = ai_settings.alien_speed
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height 
		
		self.rect.y = -100
		self.rect.x = randint(0, ai_settings.screen_width - self.rect.width)
		self.active = False
		self.hitbox = Hitbox(self)
		
	def activate(self):
		self.active =  True
		self.hitbox = Hitbox(self)
	
	def reset(self):
		self.rect.y = -100
		self.active = False
	
	def erase(self):
		if self.active:
			pygame.draw.rect(self.screen,self.ai_settings.bg_color, (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()))
		
	def blitme(self, delay):
		if self.active:
			self.rect.y += self.ai_settings.alien_speed + delay
			self.screen.blit(self.image, (self.rect.x, self.rect.y))
			if(self.rect.y > self.ai_settings.screen_height + 100):
				self.reset()
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
		self.ratio = ai_settings.screen_height/1080
		self.rect.width = self.rect.width*self.ratio
		self.rect.height = self.rect.height*self.ratio
		self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
		self.speed = ai_settings.alien_speed
		
		self.rect.y = -1000
		self.rect.x = randint(0, ai_settings.screen_width - self.rect.width)
		self.active = False
		self.hitbox = Hitbox(self)
		
	def activate(self):
		self.active =  True
		self.rect.y = -100
	
	def reset(self):
		self.rect.y = -1000
		self.active = False
	
	def erase(self):
		if self.active:
			pygame.draw.rect(self.screen,self.ai_settings.bg_color, (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()))
		
	def blitme(self, delay):
		if self.active:
			self.rect.y += self.ai_settings.alien_speed*delay
			self.screen.blit(self.image, (self.rect.x, self.rect.y))
			if(self.rect.y > self.ai_settings.screen_height + 100):
				self.reset()
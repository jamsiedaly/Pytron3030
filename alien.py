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
		
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
		
		self.y = [-100]
		self.x = [randint(0, ai_settings.screen_width - self.rect.width)]
		
		self.hitbox = Hitbox(self)
		
	def blitme(self):
		self.screen.blit(self.image, (self.x[0], self.y[0]))
		self.y[0] += self.ai_settings.alien_speed
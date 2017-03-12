import pygame
from pygame.sprite import Sprite

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
		
		self.y = -100
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, (self.x, self.y))
		
		self.y += self.ai_settings.alien_speed
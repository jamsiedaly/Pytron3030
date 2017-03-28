import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, ai_settings, screen, ship):
	
		super(Bullet, self).__init__()
		self.screen = screen
		self.settings = ai_settings
		self.rect = pygame.Rect(0, 0,
		ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.x = ship.rect.centerx
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

		
	def erase(self):
		pygame.draw.rect(self.screen, self.settings.bg_color, self.rect)

	def blitme(self):
		self.y -= self.speed_factor
		self.rect.y = self.y
		pygame.draw.rect(self.screen, self.color, self.rect)
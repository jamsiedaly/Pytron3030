import pygame
from random import randint

class Stars():

	def __init__(self, ai_settings, screen):

			self.screen = screen
			self.screen_rect =  screen.get_rect()
			self.ai_settings = ai_settings
			self.xpos = randint(0, ai_settings.screen_width)
			self.ypos = 0
			self.speed = ai_settings.star_speed
		
	def blitme(self):
	
		yellow =(100, 100, 0)
		pygame.draw.rect(self.screen, yellow, (self.xpos, self.ypos, 2, 2), 5)
		self.ypos += self.ai_settings.star_speed
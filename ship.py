import pygame
from hitbox import Hitbox

class Ship():

	def __init__(self, ai_settings, screen):
	
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('Assets/BitmapV/Ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
	
		self.rect.centerx = self.screen_rect.centerx 
		self.rect.bottom = self.screen_rect.bottom
		
		self.centerX = [float(self.rect.centerx)]
		self.centerY = [float(self.rect.centery)]
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.OriginalWidth = self.rect.width
		
	
	def erase(self):
		pygame.draw.rect(self.screen,self.ai_settings.bg_color, self.rect)
		
	def reset(self):
		self.centerX = [float(self.screen_rect.centerx)]
		self.centerY = [float(self.screen_rect.bottom)] 
		
		
	def blitme(self, delay):
		self.rect.width = self.OriginalWidth
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerX[0] += self.ai_settings.ship_speed_factor*delay
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.centerX[0] -= self.ai_settings.ship_speed_factor*delay
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centerY[0] -= self.ai_settings.ship_speed_factor*delay
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centerY[0] += self.ai_settings.ship_speed_factor*delay
		
		self.rect.centerx = self.centerX[0]
		self.rect.centery = self.centerY[0] 
		self.screen.blit(self.image, self.rect)
import pygame

class Timer():

	def __init__(self, ai_settings, screen):
	
		self.time = ai_settings.time
		self.default = ai_settings.time
		self.bg_color = ai_settings.bg_color
		self.screen = screen
		self.rect = (0, 0, 0, 0)
		self.color = (255, 255, 000)
		
	def update(self, delay):
		if self.time >= 0:
			self.time -= delay
			self.rect = (100, 920, 25, -0.2*self.time)
		else:
			self.rect = (100, 920, 25, -250)
		
	def reset(self):
		self.time = self.default
		
	def erase(self):
		pygame.draw.rect(self.screen, self.bg_color, (100, 920, 25, -250))
		
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
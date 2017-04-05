import pygame

class Timer():

	def __init__(self, ai_settings, screen):
	
		self.time = ai_settings.time
		self.default = ai_settings.time
		self.bg_color = ai_settings.bg_color
		self.screen = screen
		self.rect = (100, 700, 25, -200)
		self.color = (255, 255, 255)
		
	def update(self, delay):
		if self.time >= 0:
			self.time -= delay
			self.color = (abs(255*(self.time/self.default)),255 - abs(255*(self.time/self.default)), 0)
			self.rect = (100, 700, 25, -0.2*self.time)
		else:
			self.rect = (100, 700, 25, -200)
		
	def reset(self):
		self.time = self.default
		
	def erase(self):
		pygame.draw.rect(self.screen, self.bg_color, (100, 720, 25, -220))
		
	def blitme(self):
		print(self.color)
		print(self.time/self.default)
		pygame.draw.rect(self.screen, self.color, self.rect)
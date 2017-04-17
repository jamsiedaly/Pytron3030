import pygame

class Timer():

	def __init__(self, ai_settings, screen):
	
		self.time = ai_settings.time
		self.default = ai_settings.time
		self.bg_color = ai_settings.bg_color
		self.screen = screen
		self.screen_width = ai_settings.screen_width
		self.screen_height = ai_settings.screen_height
		self.rect = pygame.Rect( self.screen_width/15,self.screen_height/11, 25, -250)
		self.color = (255, 255, 000)
		
		
	def update(self, delay):
		if self.time >= 0:
			self.time -= delay
			self.rect.height = -self.time*0.2
		
	def reset(self):
		self.time = self.default
		
	def erase(self):
		pygame.draw.rect(self.screen, self.bg_color, ( self.screen_width/15,self.screen_height/11, 25, -250))
		
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
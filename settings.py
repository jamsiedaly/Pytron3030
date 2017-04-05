import pygame


class Settings():

	def __init__(self):
		self.info = pygame.display.Info()
		self.screen_width = 1920
		self.screen_height = 1080 
		self.bg_color = (0, 0, 20)
		self.ship_speed_factor = self.screen_width/1200
		self.star_speed = self.screen_width/5000
		self.bullet_speed_factor = self.screen_width/50
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 150, 150, 255
		self.time = 2
		self.alien_speed = self.screen_width/5000
		self.alien_frequency = 100
		self.explosionTime = 5
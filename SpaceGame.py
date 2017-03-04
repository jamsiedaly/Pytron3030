import pygame
from pygame.sprite import Group

from random import randint

from timer import Timer
from settings import Settings
from ship import Ship
from stars import Stars
from bullet import Bullet
from alien import Alien

import game_functions as gf 

def run_game():
	pygame.init()
	
	ai_settings = Settings()
	screen_height = ai_settings.screen_height
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	stars = Stars(ai_settings, screen)
	bullet = Bullet(ai_settings, screen, ship)
	star_list = [stars]
	bullets = [bullet]
	reload = Timer(ai_settings)
	alien_odds = ai_settings.alien_frequency
	aliens = []
	aliens.append(Alien(ai_settings, screen))
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, reload)
		odds = randint(0, 10)
		if reload.time >= 0:
			reload.update()
		if odds == 10:
			star_list.append(Stars(ai_settings, screen))
			stars = Stars(ai_settings, screen)
		ship.update()
		if star_list[0].ypos > screen_height:
			star_list.pop(0)
		if bullets:
			if bullets[0].y < 0:
				bullets.pop(0)
		#print(aliens[0].speed)
		gf.update_screen(ai_settings, screen, ship, star_list, bullets, aliens)
		
run_game()
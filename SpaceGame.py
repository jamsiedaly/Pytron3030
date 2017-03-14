import pygame
from pygame.sprite import Group

from random import randint

from timer import Timer
from settings import Settings
from ship import Ship
from stars import Stars
from bullet import Bullet
from alien import Alien
from hitbox import Hitbox

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
	alienHitboxes = []
	aliens.append(Alien(ai_settings, screen))
	alienHitboxes.append(Hitbox(aliens[0]))
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, reload)
		oddsStar = randint(0, 10)
		oddsAlien = randint(0, 50)
		if reload.time >= 0:
			reload.update()
		if oddsStar == 10:
			star_list.append(Stars(ai_settings, screen))
			stars = Stars(ai_settings, screen)
		if oddsAlien == 10:
			aliens.append(Alien(ai_settings, screen))
			#alienHitboxes.append(Hitbox(aliens))
		ship.update()
		if star_list[0].ypos > screen_height:
			star_list.pop(0)
		if aliens:
			if aliens[0].y[0] > screen_height:
				aliens.pop(0)
		if bullets:
			if bullets[0].y < 0:
				bullets.pop(0)
		print(alienHitboxes[0].y)
		print(aliens[0].y)
		gf.update_screen(ai_settings, screen, ship, star_list, bullets, aliens)
		
run_game()
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
from explosion import Explosion

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
	explosions = []
	refreshFPS = 10
	avgFPS = 0
	while True:
		start = pygame.time.get_ticks()
		gf.check_events(ai_settings, screen, ship, bullets, reload)
		oddsStar = randint(0, 10)
		oddsAlien = randint(0, 50)
		
		for e in aliens:
			for b in bullets:
				if e.hitbox.y1[0][0] <= b.y  and b.y <= e.hitbox.y2() and e.hitbox.x1[0][0] <= b.x and b.x <= e.hitbox.x2():
					bullets.remove(b)
					explosions.append(Explosion(e))
					aliens.remove(e)
		
		if reload.time >= 0:
			reload.update()
		if oddsStar >= 4:
			star_list.append(Stars(ai_settings, screen))
		if oddsAlien == 10:
			aliens.append(Alien(ai_settings, screen))
		ship.update()
		if star_list[0].ypos > screen_height:
			star_list.pop(0)
		if aliens:
			if aliens[0].rect.y > screen_height:
				aliens.pop(0)
		if bullets:
			if bullets[0].y < 0:
				bullets.pop(0)
		
		gf.update_screen(ai_settings, screen, ship, star_list, bullets, aliens, explosions)
		finish = pygame.time.get_ticks()
		delay = finish - start
		
		
		fps = 1000/delay
		if(refreshFPS == 0):
			screen.fill(ai_settings.bg_color, (100,100, 100,100))
			myfont = pygame.font.SysFont("monospace", 15)
			label = myfont.render(str(int(avgFPS)), 1, (255,255,0))
			screen.blit(label, (100, 100))
			refreshFPS = 10
			avgFPS = 0
			
		else:
			refreshFPS -= 1
			avgFPS += fps/10
run_game()
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
	
	clock = pygame.time.Clock()
	clock.tick()
	ai_settings = Settings()
	screen_height = ai_settings.screen_height
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height),pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
	screen.fill(ai_settings.bg_color, (0,0,ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	stars = Stars(ai_settings, screen)
	bullet = Bullet(ai_settings, screen, ship)
	starIndex = 0
	star_list = [Stars(ai_settings, screen) for i in range(200)]
	alienFrequency = 0
	alienIndex = 0
	aliens = [Alien(ai_settings, screen) for i in range(200)]
	bullets = [bullet]
	reload = Timer(ai_settings)
	alien_odds = ai_settings.alien_frequency
	explosions = []
	refreshFPS = 10
	avgFPS = 0
	delay = 0
	pygame.mixer.music.load('Assets/Sounds/explosion.mp3')
	while True:
		alienFrequency = int(pygame.time.get_ticks() / 10000)
		clock.tick()
		delay = clock.get_time()
		gf.check_events(ai_settings, screen, ship, bullets, reload)
		oddsStar = randint(0, 10)
		oddsAlien = randint(0, 50)
		
		for alien in aliens:
			if pygame.sprite.collide_rect(ship, alien):
				pygame.mixer.music.play(0)
				explosions.append(Explosion(ship))
		
		for e in aliens:
			for b in bullets:
				if e.hitbox.y1[0] <= b.y  and b.y <= e.hitbox.y2() and e.hitbox.x1[0]<= b.x and b.x <= e.hitbox.x2() and e.active:
					pygame.mixer.music.play(0)
					bullets.remove(b)
					explosions.append(Explosion(e))
					e.erase()
					e.reset()
		
		if reload.time >= 0:
			reload.update()
		if oddsStar == 10:
			star_list[starIndex%200].activate()
			starIndex += 1
		if oddsAlien <= alienFrequency:
			aliens[alienIndex%200].activate()
			alienIndex += 1
		if bullets:
			if bullets[0].y < 0:
				bullets.pop(0)
		
		gf.update_screen(ai_settings, screen, ship, star_list, bullets, aliens, explosions, delay)
		screen.fill(ai_settings.bg_color, (0,0, 30,30))
		myfont = pygame.font.SysFont("monospace", 15)
		label = myfont.render(str(int(clock.get_fps())), 1, (255,255,0))
		screen.blit(label, (0,0))

run_game()
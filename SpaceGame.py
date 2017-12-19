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
	
	numberOfLives = 3
	clock = pygame.time.Clock()
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
	reload = Timer(ai_settings, screen)
	alien_odds = ai_settings.alien_frequency
	explosions = []
	refreshFPS = 10
	avgFPS = 0
	delay = 0
	pygame.mixer.music.load('Assets/Sounds/explosion.mp3')
	myfont = pygame.font.SysFont("monospace", 10)
	livesfont = pygame.font.SysFont("monospace", 30)
	gameOver = pygame.font.SysFont("monospace", 60)
	UI_color = (100, 100, 110)
	pause = 0
	paused = False
	gameOverMessage = ""
	while True:
		gf.update_screen(ai_settings, screen, ship, star_list, bullets, aliens, explosions, reload ,delay)
		alienFrequency = int(pygame.time.get_ticks() / 10000)
		clock.tick()
		delay = clock.get_time()
		gf.check_events(ai_settings, screen, ship, bullets, reload)
		if pause <= 0 and paused:
			paused = False
			numberOfLives = 3
			ship.reset()
			gameOverMessage = ""
			screen.fill(ai_settings.bg_color, (700,450, 600,200))
			alienFrequency = 0
			
		else:
			pause -= delay
		
		if paused == False:
			oddsStar = randint(0, 10)
			oddsAlien = randint(0, 50)
		
		for alien in aliens:
			if pygame.sprite.collide_rect(ship, alien):
				alien.erase()
				alien.reset()
				pygame.mixer.music.play(0)
				explosions.append(Explosion(ship))
				numberOfLives -= 1
				if numberOfLives == 0:
					ship.erase()
					ship.centerX[0] = -10000
					gameOverMessage = "GAME OVER!!!"
					for alien in aliens:
						explosions.append(Explosion(alien))
						alien.erase()
						alien.reset()
						pause = 3000
						paused = True
		
		for alien in aliens:
			for bullet in bullets:
				if alien.rect.collidepoint(bullet.rect.x, bullet.rect.y):
					pygame.mixer.music.play(0)
					explosions.append(Explosion(alien))
					bullets.remove(bullet)
					alien.erase()
					alien.reset()
				
				
		reload.update(delay)
		if oddsStar == 10:
			star_list[starIndex%200].activate()
			starIndex += 1
		if oddsAlien <= alienFrequency:
			aliens[alienIndex%200].activate()
			alienIndex += 1
		if bullets:
			if bullets[0].y < 0:
				bullets[0].erase()
				bullets.pop(0)
		
		screen.fill(UI_color, (0,0, 100,100))
		label = myfont.render(str(int(clock.get_fps())), 1, (255,255,0))
		lives = myfont.render("LIVES REMAINING :", 1, (255,255,0))
		remaining = livesfont.render(str(numberOfLives), 1, (255,255,0))
		gg = gameOver.render(gameOverMessage, 1, (255,255,0))
		screen.blit(label, (0,0))
		screen.blit(lives, (0,30))
		screen.blit(remaining, (20,45))
		screen.blit(gg, (700,450))
		pygame.display.flip()
run_game()
import sys
from bullet import Bullet
import pygame 

def check_events(ai_settings, screen, ship, bullets, reload):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets, reload)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def check_keydown_events(event, ai_settings, screen, ship, bullets, reload):	
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True			
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		if reload.time < 1:
			reload.reset()
			bullets.append(Bullet(ai_settings, screen, ship))
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
				
def update_screen(ai_settings, screen, ship, star_list, bullets, aliens, explosions):
	
	for stars in star_list:
		stars.erase()
	ship.erase()
	for bullet in bullets:
		bullet.erase()
	for alien in aliens:
		alien.erase()
	for explosion in explosions:
		explosion.erase()
	for stars in star_list:
		stars.blitme()
	ship.blitme()
	for bullet in bullets:
		bullet.blitme()
	for alien in aliens:
		alien.blitme()
	for explosion in explosions:
		if explosion.blitme():
			pass
		else:
			explosions.remove(explosion)
		
	pygame.display.flip()
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
# from alien import Alien

def run_game():
	#Initilize pygame, settings, and screen object.
	pygame.init()
	# screen = pygame.display.set_mode((1200, 800))
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	pygame.display.set_caption("Alien Invasion - By Kunal")

	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game statistics and create a scoreboade.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#Make a ship, a group of biullets and a group of aliens.
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group() #<-Alien(ai_settings, screen)

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Start the main loop for game.
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		# bullets.update()

		# for bullet in bullets.copy():
		# 	if bullet.rect.bottom <= 0:
		# 		bullets.remove(bullet)
		# print(len(bullets))

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()


"""
(: (: (: FINALYYY FINISH :- 23/07/2020 :) :) :)
"""
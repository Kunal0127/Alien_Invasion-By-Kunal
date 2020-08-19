import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect(rectangle).
		self.image = pygame.image.load('images/img2.bmp')
		self.rect = self.image.get_rect()
		# self.pseudo_rect = self.rect.inflate(5, 5)
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False



	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's center value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		if self.moving_up and self.rect.top > 0:
			self.bottom -= self.ai_settings.ship_speed_factor

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor

		# update rect object from self.center
		self.rect.centerx = self.center
		self.rect.bottom = self.bottom

	def center_ship(self):
		""" Bottom-Center the ship on the screen when the ship hit the aliens."""
		self.center = self.screen_rect.centerx
		self.bottom = self.screen_rect.bottom


	def blitem(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
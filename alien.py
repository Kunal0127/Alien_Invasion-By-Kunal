import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent asingle alien in the fleet."""
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		# load the alien image and set its rect attribute.
		self.image = pygame.image.load('images/img1.bmp')
		self.rect = self.image.get_rect()

		# Start each new alien near the top of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien exect position.
		self.x = float(self.rect.x)

	def check_edges(self):
			""" Return True if alien is at edge of screen."""	
			screen_rect = self.screen.get_rect()
			if self.rect.right >= screen_rect.right:
				return True
			elif self.rect.left <= 0:
				return True

	def update(self):
		"""Move the alien right or left."""
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def blitem(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)

		
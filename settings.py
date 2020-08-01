class Settings():
	"""A class the store all settings for Alien Invention."""
	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1100
		self.screen_height = 680
		self.bg_color = (255, 255, 255)
	   # Ship settings
		# self.ship_speed_factor = 1.5
		self.ship_limit = 3
	   # Bullet settings
		# self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 12
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
	   # Alien settings
		# self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		# self.fleet_direction = 1
	   # How quickly the game speed up.
		self.speedup_scale = 1.1
	   # How quickly the alien pointvalue increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughtout the game."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 1

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Scoring.
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

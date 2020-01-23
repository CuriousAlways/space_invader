

class Settings :
	'''class which contains game settings'''
	def __init__(self) :
		#game window setting
		self.width    = 850
		self.height   = 400
		self.bg_color =(230,230,230) 

		#ship settings
		self.ship_speed = 1.5

		#bullet settings
		self.bullet_speed  = 0.1
		self.bullet_width  = 2
		self.bullet_height = 7
		self.bullet_color  = (60,60,60)
		self.no_allowed_bullets = 2

		#aliens settings
		self.alien_speed_x = 0.5
		self.alien_speed_y = 50

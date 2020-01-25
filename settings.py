

class Settings :
	'''class which contains game settings'''
	def __init__(self) :
		#game window setting
		self.width    = 850
		self.height   = 400
		self.bg_color =(230,230,230) 

		#ship settings
		self.no_of_ship = 3

		#bullet settings
		self.bullet_speed  = 0.1
		self.bullet_width  = 2
		self.bullet_height = 7
		self.bullet_color  = (60,60,60)
		self.no_allowed_bullets = 2

		#aliens settings
		self.alien_speed_x = 0.5
		self.alien_speed_y = 50

		#determines by how much does the dynamic quantity would change
		self.speed_up_factor = 1.1


	def dynamic_settings(self) :
		#values of these quantity can change during game play
		self.ship_speed      = 1.5
		self.bullet_speed    = 0.1
		self.alien_speed_x   = 0.5
		self.alien_hit_point = 10   #points user get on hitting an alien


	def level_up(self) :
		#changes values of dynamic settings as game progresses
		self.ship_speed      *= self.speed_up_factor
		self.bullet_speed    *= self.speed_up_factor
		self.alien_speed_x   *= self.speed_up_factor
		self.alien_hit_point += 2





import pygame

class Ship:
	'''this class controls all aspects of ship'''

	def __init__(self,si_game) :
		'''to get access to attributes and method defined
		in Space_invader class it has second parameter'''

		self.screen = si_game.screen  
		#getting rect attribute of game window 
		self.screen_rect = self.screen.get_rect() 

		#getting settings
		self.setting = si_game.setting

		#loading image
		self.image = pygame.image.load('./images/ship.bmp') 

		#getting rect attribute of surface object(here ship image)
		self.image_rect = self.image.get_rect()   
		#alligning ship image so that it appears at bottom center
		self.image_rect.midbottom = self.screen_rect.midbottom

		#movement flags and speed 
		self.ship_speed = si_game.setting.ship_speed
		self.move_right = False
		self.move_left  = False
		self.move_up    = False
		self.move_down  = False



	def draw_ship(self) :
		'''draws ship on game window according to its rect attribute value'''
		self.screen.blit(self.image,self.image_rect)


	def move_ship(self) :
		'''moves ship after evaluating flags'''
		self.loc_x = float(self.image_rect.x)
		self.loc_y = float(self.image_rect.y)

		if (self.move_right and self.image_rect.right <= self.setting.width):
			self.loc_x += self.ship_speed

		if (self.move_left and self.image_rect.left >= 0):
			self.loc_x -= self.ship_speed 

		if (self.move_up and self.image_rect.top >= 0):
			self.loc_y -= self.ship_speed 

		if (self.move_down and self.image_rect.bottom <= self.setting.height):
			self.loc_y += self.ship_speed


		self.image_rect.x = self.loc_x
		self.image_rect.y = self.loc_y




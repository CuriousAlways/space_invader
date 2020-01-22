import pygame

class Ship:
	'''this class controls all aspects of ship'''

	def __init__(self,si_game) :
		'''to get access to attributes and method defined
		in Space_invader class it has second parameter'''

		self.screen = si_game.screen   
		self.screen_rect = self.screen.get_rect()  #getting rect attribute of game window

		self.image = pygame.image.load('./images/ship.bmp') #returns a surface object 
		self.image_rect = self.image.get_rect()   #getting rect attribute of surface object(here ship image)

		self.image_rect.midbottom = self.screen_rect.midbottom  #alligning ship image so that it appears at bottom center

	def draw_ship(self) :
		'''draws ship on game window according to its rect attribute value'''

		self.screen.blit(self.image,self.image_rect)

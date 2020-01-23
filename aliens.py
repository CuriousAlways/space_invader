import pygame
from pygame.sprite import Sprite

class Alien(Sprite) :
	'''This class  manages all aspect of alien fleet'''
	def __init__(self,si_game) :
		
		super().__init__()

		self.screen  = si_game.screen
		self.setting = si_game.setting

		#load and get rect attrubute of aliens
		self.alien_image = pygame.image.load("./images/alien.bmp")
		self.alien_rect  = self.alien_image.get_rect()

		#set position of aliens shift toward left and down equal to its width and height  
		self.alien_rect.x = self.alien_rect.width
		self.alien_rect.y = self.alien_rect.height

		#needed by pygame.sprite.groupcollide() used in space_invader.py
		self.rect = self.alien_rect

		#store x coordinate of aliens
		self.x = float(self.alien_rect.x)

		#direction of movement of alien(just to control each ship movement individually)
		self.direction = 1 

	#drawing alien
	def draw_alien(self):
		self.screen.blit(self.alien_image,self.alien_rect)

	#moving alien
	def move_alien(self):
		self._check_direction()
		self.x += (self.direction*self.setting.alien_speed_x)
		self.alien_rect.x =self.x


	#check the direction
	def _check_direction(self) :
		self.screen_rect = self.screen.get_rect()
		if (self.alien_rect.right >= self.screen_rect.right or self.alien_rect.left <= 0):
			self.direction *= -1 
			self.alien_rect.y += self.setting.alien_speed_y



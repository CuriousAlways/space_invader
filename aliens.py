import pygame
from pygame.sprite import Sprite

class Alien(Sprite) :
	'''This class  manages all aspect of alien fleet'''
	def __init__(self,si_game) :
		
		super().__init__()

		self.screen = si_game.screen

		#load and get rect attrubute of aliens
		self.alien_image = pygame.image.load("./images/alien.bmp")
		self.alien_rect  = self.alien_image.get_rect()

		#set position of aliens shift toward left and down equal to its width and height  
		self.alien_rect.x = self.alien_rect.width
		self.alien_rect.y = self.alien_rect.height

		#store x coordinate of aliens
		self.x = float(self.alien_rect.x)

		#drawing alien
	def draw_alien(self):
		self.screen.blit(self.alien_image,self.alien_rect)

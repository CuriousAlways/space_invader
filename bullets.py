import pygame
from pygame.sprite import Sprite

class Bullet(Sprite) :
	'''bullet class that handles drawing and bullet movement'''

	def __init__(self,si_game) :
		#initializes Sprite class
		super().__init__()
		#creating class variable for various object from SpaceInavder class
		self.screen         = si_game.screen
		self.bullet_setting = si_game.setting
		self.bullet_color   = si_game.setting.bullet_color

		#creating a rectangular bullet at (0,0) and specified width and height
		self.bullet_rect = pygame.Rect(0,0,self.bullet_setting.bullet_width,self.bullet_setting.bullet_height)
		#relocating the bullet to the top of ship
		self.bullet_rect.midtop = si_game.ship.image_rect.midtop


	def move_bullet(self) :
		'''moving bullet upwards at specified speed'''
		bullet_y  = float(self.bullet_rect.y)
		bullet_y -= self.bullet_setting.bullet_speed
		self.bullet_rect.y = bullet_y


	def draw_bullet(self) :
		'''draws bullet on the screen '''
		pygame.draw.rect(self.screen,self.bullet_color,self.bullet_rect)


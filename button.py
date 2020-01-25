import pygame.font

class Button():
	'''creates play button'''
	def __init__(self,si_game,msg):

		self.screen      = si_game.screen
		self.screen_rect = self.screen.get_rect()

		#button attribute
		self.button_width = 250
		self.button_hight = 60
		self.button_color = (0,255,0)
		self.text_color   = (255,255,255) 
		self.font         = pygame.font.SysFont(None, 48)

		#creating a rect object that would be later used to draw the button
		self.button_rect        = pygame.Rect(0,0,self.button_width,self.button_hight)
		self.button_rect.center = self.screen_rect.center

		#draws button with specified image
		self._render_msg(msg) 


	def _render_msg(self,msg):
		'''pygame renders text to be displayed by rendering it as image'''
		
		self.msg_image              = self.font.render(msg,True,self.text_color,self.button_color) #return an image with specified text and background color
		self.msg_image_rect         = self.msg_image.get_rect()
		self.msg_image_rect.center  = self.button_rect.center


	def draw_button(self):
		'''draws button to screen'''
		self.screen.fill(self.button_color,self.button_rect) #fills the specified region(self.button_rect) with color(self.button_color), if region is not specified the whole screen is filled with the color 
		self.screen.blit(self.msg_image,self.msg_image_rect)		
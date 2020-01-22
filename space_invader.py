import sys
import pygame
from settings import Settings 
from ship import Ship

class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		self.setting = Settings() 

		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((self.setting.width,self.setting.height)) #creates the game window
		pygame.display.set_caption('Space Invader')

		self.ship = Ship(self)

	def run_game(self) :

		while True:
			self._check_event()
			self._update_screen()  

	def _check_event(self) :

		#an event loop to recognise user action
			for event in pygame.event.get():  
				print(f'event : {event}')     #just a debug statement 
				# identifying the event if game's close window button is pressed 
				if (event.type == pygame.QUIT) :  
					sys.exit()

	def _update_screen(self) :

		#gives background color to game window by redrawing screen on every loop 
		self.screen.fill(self.setting.bg_color)
		#draws ship on screen
		self.ship.draw_ship() 
		#drawing the screen with updated game element states
		pygame.display.flip()
			




if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


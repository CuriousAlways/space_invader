import sys
import pygame
from settings import Settings 
from ship import Ship

class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		self.setting = Settings() 

		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((self.setting.width,self.setting.height),pygame.RESIZABLE) #creates the game window
		pygame.display.set_caption('Space Invader')

		self.ship = Ship(self)

	def run_game(self) :

		while True:
			self._check_event()
			self.ship.move_ship()
			self._update_screen()
			#debug statement
			print(f'width :{self.setting.width}  , height :{self.setting.height}')  

	def _check_event(self) :

		#an event loop to recognise user action
			for event in pygame.event.get():  
				#print(f'event : {event}')     #just a debug statement 
				# identifying the event if game's close window button is pressed 
				if (event.type == pygame.QUIT) :  
					sys.exit()

				elif (event.type == pygame.KEYDOWN):
					self._keydown_event_check(event) #identify if some key is pressed

				elif (event.type == pygame.KEYUP):
					self._keyup_event_check(event) #identify if some key is released

				elif (event.type == pygame.VIDEORESIZE):
					self.setting.width  = event.w
					self.setting.height = event.h
					self.screen = pygame.display.set_mode((self.setting.width,self.setting.height),pygame.RESIZABLE)




	def _update_screen(self) :

		#gives background color to game window by redrawing screen on every loop 
		self.screen.fill(self.setting.bg_color)
		#draws ship on screen
		self.ship.draw_ship() 
		#drawing the screen with updated game element states
		pygame.display.flip()


	def _keydown_event_check(self,event) :
		if (event.key == pygame.K_RIGHT)   :
			self.ship.move_right = True

		elif (event.key == pygame.K_LEFT)  :
			self.ship.move_left = True

		elif (event.key == pygame.K_UP)    :
			self.ship.move_up   = True

		elif (event.key == pygame.K_DOWN)  :
			self.ship.move_down = True

		elif (event.key == pygame.K_q)     :
			sys.exit()


	def _keyup_event_check(self,event) :
		if (event.key == pygame.K_RIGHT)   :
			self.ship.move_right = False

		elif (event.key == pygame.K_LEFT)  :
			self.ship.move_left = False

		elif (event.key == pygame.K_UP)    :
			self.ship.move_up   = False

		elif (event.key == pygame.K_DOWN)  :
			self.ship.move_down = False
			




if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


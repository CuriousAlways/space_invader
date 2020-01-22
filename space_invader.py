import sys
import pygame


class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((1200,800)) #creates the game window
		pygame.display.set_caption('Space Invader')
		self.bg_color = (200,200,200)

	def run_game(self) :

		while True:

			#an event loop to recognise user action
			for event in pygame.event.get():  
				print(f'event : {event}')     #just a debug statement

				# identifying the event if game's close window button is pressed 
				if (event.type == pygame.QUIT) :  
					sys.exit()

			#gives background color to game window by redrawing screen on every loop 
			self.screen.fill(self.bg_color) 
			#drawing the screen with updated game element states
			pygame.display.flip()  



if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


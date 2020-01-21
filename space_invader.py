import sys
import pygame


class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((1200,800)) #creates the game window
		pygame.display.set_caption('Space Invader')

	def run_game(self) :

		while True:

			for event in pygame.event.get():  #an event loop to recognise user action
				print(f'event : {event}')     #just a debug statement

				if (event.type == pygame.QUIT) :  # identifying the event if game's close window button is pressed 
					sys.exit()

			pygame.display.flip()  #drawing the screen with updated game element states



if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


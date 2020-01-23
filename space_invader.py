import sys
import pygame
from settings import Settings 
from ship import Ship
from bullets import Bullet
from aliens import Alien

class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		self.setting = Settings() 

		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((self.setting.width,self.setting.height),pygame.RESIZABLE) #creates the game window
		pygame.display.set_caption('Space Invader')

		self.ship = Ship(self)

		#container class to manage multiple object (bullet) of pygame.Sprite type
		self.bullets = pygame.sprite.Group()

		#container class to manage multiple object (bullet) of pygame.Sprite type
		self.aliens = pygame.sprite.Group()
		self._create_alien_fleet()

	def run_game(self) :

		while True:
			self._check_event()

			self.ship.move_ship()
			#calls move_bullet method for each sprite object
			for bullet in self.bullets.sprites():
				bullet.move_bullet()

			#remove bullets that went beyond the game window
			self._remove_bullets()

			self._update_screen()
			#debug statement
			#print(f'width :{self.setting.width}  , height :{self.setting.height}')


	def _create_alien_fleet(self):
		#create a dummy alien ship to manage spacing on screen
		alien = Alien(self) 
		alien_width = alien.alien_rect.width

		#calculate no. of aliens that can be drawn on game window
		available_space = self.setting.width - 2*alien_width
		no_of_alien = available_space // (2*alien_width)

		#creating Alien object and adding them to pygame.sprite.Group()
		for alien_number in range(no_of_alien) :
			alien = Alien(self)
			alien.x = alien_width + 2*alien_number*alien_width
			alien.alien_rect.x = alien.x
			self.aliens.add(alien)

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
		#draw alien ships
		for alien in self.aliens.sprites():
			alien.draw_alien()
		#draws bullet on screen
		for bullet in self.bullets.sprites():
			bullet.draw_bullet() 
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

		elif (event.key == pygame.K_SPACE) :
			self._fire_new_bullet()


	def _keyup_event_check(self,event) :
		if (event.key == pygame.K_RIGHT)   :
			self.ship.move_right = False

		elif (event.key == pygame.K_LEFT)  :
			self.ship.move_left = False

		elif (event.key == pygame.K_UP)    :
			self.ship.move_up   = False

		elif (event.key == pygame.K_DOWN)  :
			self.ship.move_down = False


	def _fire_new_bullet(self) :
		if (len(self.bullets) <= self.setting.no_allowed_bullets) :
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)


	def _remove_bullets(self) :
		#we cannot remove element and iterate simultaneously hence we are working on copy
		for bullet in self.bullets.copy() :
			if bullet.bullet_rect.bottom < 0:
				self.bullets.remove(bullet)
		#debug line
		print(f"bullet -{len(self.bullets)}")
			




if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


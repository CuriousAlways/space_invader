import sys
import pygame
from time import sleep
from game_stats import Game_Stats
from settings import Settings 
from ship import Ship
from bullets import Bullet
from aliens import Alien
from button import Button
from scoreboard import Score_Board




class Space_Invader :
	'''class to manage game resources and assets'''
	def __init__(self) :

		self.setting = Settings() 


		pygame.init(); #initializes background setting of pygame
		self.screen = pygame.display.set_mode((self.setting.width,self.setting.height),pygame.RESIZABLE) #creates the game window
		pygame.display.set_caption('Space Invader')


		self.game_stats = Game_Stats(self)


		self.ship = Ship(self)

		#container class to manage multiple object (bullet) of pygame.Sprite type
		self.bullets = pygame.sprite.Group()

		#container class instance to manage multiple object (bullet) of pygame.Sprite type
		self.aliens = pygame.sprite.Group()
		self._create_alien_fleet()

		#create a button instance
		self.button = Button(self,'Play')

		#instance of Score_Board() class 
		self.scoreboard = Score_Board(self)


	def run_game(self) :

		while True:
			self._check_event()

			if self.game_stats.game_active :
				
				for alien in self.aliens.sprites():
					alien.move_alien()

				self.ship.move_ship()
				#calls move_bullet method for each sprite object
				for bullet in self.bullets.sprites():
					bullet.move_bullet()

				#remove bullets that went beyond the game window
				self._remove_bullets()

				#when all of the fleet is destroyed we redraw the fleet
				if not self.aliens : #empty group evaluates False
					self.setting.level_up()
					self._create_alien_fleet()
			# else:
			# 	print("GAME OVER!!!")

			self._update_screen()
			#debug statement
			#print(f'width :{self.setting.width}  , height :{self.setting.height}')



	def _create_alien_fleet(self):
		#create a dummy alien ship to manage spacing on screen
		alien = Alien(self) 

		alien_width = alien.alien_rect.width
		alien_height = alien.alien_rect.height

		#calculate no. of aliens that can be drawn in a row on game window
		available_space = self.setting.width - 2*alien_width
		no_of_alien = available_space // (2*alien_width)

		#calculate no. of rows of aliens that can be drawn 
		available_space = self.setting.height - 3*alien_height -self.ship.image_rect.height
		no_of_row = available_space//(2*alien_height)
		#print("no. of rows "+str(no_of_row)) #debug statement

		#creating Alien object and adding them to pygame.sprite.Group()
		for row_no in range(no_of_row):
			for alien_number in range(no_of_alien) :
				self._create_alien(row_no,alien_number)
			


	def _create_alien(self,row_no,alien_number):
		alien = Alien(self)
		alien_width = alien.alien_rect.width
		alien_height = alien.alien_rect.height
		alien.y = alien_height + 2*alien_height*row_no
		alien.x = alien_width + 2*alien_number*alien_width
		alien.alien_rect.y = alien.y
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

				elif (event.type == pygame.MOUSEBUTTONDOWN):
					mouse_pos = pygame.mouse.get_pos() # returns tuple with mouse x,y coordinate
					self._check_play_button(mouse_pos) #checks if play button is pressed




	def _update_screen(self) :

		#gives background color to game window by redrawing screen on every loop 
		self.screen.fill(self.setting.bg_color)

		#draws ship on screen
		self.ship.draw_ship()

		#draw alien ships
		for alien in self.aliens.sprites():
			alien.draw_alien()

		#detecting collision between ship and alien
		if pygame.sprite.spritecollideany(self.ship,self.aliens): #returns alien that collided else None
			self._ship_hit()

		#draws bullet on screen
		for bullet in self.bullets.sprites():
			bullet.draw_bullet() 

		#removing bullet and aliens that had collided
		'''any bullet that collides with an alien becomes 
		a key in the collisions dictionary. The value associated 
		with each bullet is a list of aliens it has collided with'''
		collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

		if collision:
			for alien in collision.values():
				self.game_stats.current_score += (self.setting.alien_hit_point * len(alien))

		#updating high score
		if self.game_stats.current_score > self.scoreboard.high_score :
			Score_Board.update_high_score(self.game_stats.current_score)    #update_high_score() is defined in game_stats.py

		#number lifes user have indicated by ship image on top right corner
		self.life_indicator()

		#prints score
		self.scoreboard.draw_score(self.game_stats.current_score)

		#display button initially or when self.game_stats.game_active = False
		if self.game_stats.game_active == False:
			self.button.draw_button()

		#drawing the screen with updated game element states
		pygame.display.flip()

		#detecting if any ship reached bottom
		self.alien_reaches_bottom()



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

		elif ((event.key == pygame.K_SPACE) and (self.game_stats.game_active)): #rest of KEYDOWN events remain inactive because in run_game loop neither alien nor ship is repositioned until game_status_active become true
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

	def _check_play_button(self,mouse_pos):
		button_clicked = self.button.button_rect.collidepoint(mouse_pos)
		if (button_clicked and not self.game_stats.game_active) :
			self.game_stats.reset_stats()
			self.game_stats.game_active = True
			


	def _fire_new_bullet(self) :
		if (len(self.bullets) <= self.setting.no_allowed_bullets) :
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)



	def _remove_bullets(self) :
		#we cannot remove element and iterate simultaneously hence we are working on copy
		for bullet in self.bullets.copy() :
			if bullet.bullet_rect.top <= 0:
				#print('--removing bullet---')#debug
				self.bullets.remove(bullet)
		#debug line
		#print(f"bullet -{len(self.bullets)}")


	def alien_reaches_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			alien_rect = alien.alien_rect
			if(alien_rect.bottom >= screen_rect.bottom):
				#this is same as though ship is hit by alien
				self._ship_hit()	

	def _ship_hit(self):
		#pause game for 1 sec
		sleep(1)

		#decrement no. of ships left
		self.game_stats.no_of_ship_left -= 1

		#clear game window	
		self.aliens.empty()
		self.bullets.empty()

		#redraw fleet and reposition ship 
		self._create_alien_fleet()
		self.ship.reposition_ship(self)

		#if no. of ship left = 0 then gameover
		if self.game_stats.no_of_ship_left == 0:
			self.game_stats.game_active = False
			print("GAME OVER!!!")



	def life_indicator(self):
		'''displays no. of before game over at top right corner'''
		for count in range(self.game_stats.no_of_ship_left):
			#print('count = '+str(count))#debug line
			image       = pygame.image.load('./images/ship_indicator.bmp')
			image_rect  = image.get_rect()
			screen_rect = self.screen.get_rect()
			image_rect.top   = screen_rect.top
			image_rect.right = screen_rect.right - count*image_rect.width
			self.screen.blit(image,image_rect)





if __name__ == '__main__':

	si = Space_Invader()

	si.run_game()


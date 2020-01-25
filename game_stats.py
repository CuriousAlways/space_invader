
class Game_Stats :
	'''Track statistics for game'''
	def __init__(self,si_game):

		self.setting     = si_game.setting
		
		#starts game in inactive state
		self.game_active = False

		#reset various game component
		self.reset_stats()


	def reset_stats(self) :
		self.no_of_ship_left = self.setting.no_of_ship
		self.current_score   = 0  #player score is zero (initially and after restart) 
		self.setting.dynamic_settings()
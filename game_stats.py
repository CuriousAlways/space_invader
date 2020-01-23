
class Game_Stats :
	'''Track statistics for game'''
	def __init__(self,si_game):

		self.setting     = si_game.setting
		self.game_active = True
		self.reset_stats()


	def reset_stats(self) :
		self.no_of_ship_left = self.setting.no_of_ship
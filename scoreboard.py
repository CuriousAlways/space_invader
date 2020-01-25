import pygame.font

class Score_Board():
	'''this class handles all aspects of scoring'''
	def __init__(self, si_game):

		self.screen      = si_game.screen
		self.screen_rect = self.screen.get_rect()
		self.bg_color    = si_game.setting.bg_color

		self.text_color  = (255,100,0)
		self.font        = pygame.font.SysFont(None,40)


	def _render_score(self,score):
		'''renders score's image'''
		self.score_image      = self.font.render(str(score),True,self.text_color,self.bg_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.top  = self.screen_rect.top + 5
		self.score_image_rect.left = self.screen_rect.left +10


	def draw_score(self,score):
		'''draws score on the screen'''
		self._render_score(score)
		self.screen.blit(self.score_image,self.score_image_rect)


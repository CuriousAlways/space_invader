import pygame.font
import json

class Score_Board():
	'''this class handles all aspects of scoring'''
	def __init__(self, si_game):

		self.screen      = si_game.screen
		self.screen_rect = self.screen.get_rect()
		self.bg_color    = si_game.setting.bg_color

		self.text_color  = (255,100,0)
		self.font        = pygame.font.SysFont(None,40)

		self.high_score_color = (0,0,0)
		self.high_score  = self._get_high_score()


	def _render_score(self,score):
		'''renders score's image'''
		self.score_image      = self.font.render(str(score),True,self.text_color,self.bg_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.top  = self.screen_rect.top + 5
		self.score_image_rect.left = self.screen_rect.left +10


	def _render_high_score(self):
		'''renders high score's image'''
		self.high_score = self._get_high_score()
		self.hscore_image      = self.font.render(str(self.high_score),True,self.high_score_color,self.bg_color)
		self.hscore_image_rect = self.hscore_image.get_rect()
		self.hscore_image_rect.midtop  = self.screen_rect.midtop
		self.hscore_image_rect.top = self.screen_rect.top + 5


	def draw_score(self,score):
		'''draws score on the screen'''
		self._render_score(score)
		self._render_high_score()

		self.screen.blit(self.score_image,self.score_image_rect)
		self.screen.blit(self.hscore_image,self.hscore_image_rect)


	def _get_high_score(self) :
		with open('./highscore.json','r') as high_score_file :
			return json.load(high_score_file)


	@staticmethod
	def update_high_score(new_high_score):
		with open('./highscore.json','w') as high_score_file :
			json.dump(new_high_score,high_score_file)




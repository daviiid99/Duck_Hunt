from resources import *
from board import *
import threading
import time
import json


vec = pygame.math.Vector2

def write_json() :

	data = json.dumps(save)

	with open('save.json', 'w') as s :
		s.write(data)


class Mode :

	def __init__(self) :
		self.running = True
		self.screen = WIN
		self.clock = pygame.time.Clock()
		self.screen_rect = self.screen.get_rect()
		self.mouse = vec()
		self.choosing_mode = True
		self.mode_1_rect = pygame.Rect(50, 200, 300, 300)
		self.mode_2_rect = pygame.Rect(500, 200, 300, 300)

	def check_mouse(self, mouse) :

		if self.mode_1_rect.collidepoint(mouse) :
			save["GAME"]["PLAYER_MODE"] = 1
			self.choosing_mode = False
			write_json()
			board = Board()
			board.start_game()

		elif self.mode_2_rect.collidepoint(mouse) :
			save["GAME"]["PLAYER_MODE"] = 2
			self.choosing_mode = False
			write_json()
			board = Board()
			board.start_game()

	def draw_screen (self) :

		while self.choosing_mode :

			# Draw background
			self.screen.blit(modes_bg, (0,0))

			# Draw modes buttons
			self.screen.blit(black_bg, (self.mode_1_rect.x + 10, self.mode_1_rect.y))
			self.screen.blit(mode_1, (self.mode_1_rect.x, self.mode_1_rect.y))
			
			self.screen.blit(black_bg, (self.mode_2_rect.x + 10, self.mode_2_rect.y))
			self.screen.blit(mode_2, (self.mode_2_rect.x, self.mode_2_rect.y))


			# Modes dialog
			text = MEDIUM_FONT.render("1 Duck", 1, WHITE)
			self.screen.blit(text, (145, 205))

			text = MEDIUM_FONT.render("2 Ducks", 1, WHITE)
			self.screen.blit(text, (585, 210))

			# Draw dialog button
			self.screen.blit(dialog, (260, 40))

			# Dialog text
			text = SUBTITLE_FONT.render("CHOOSE", 1, WHITE)
			self.screen.blit(text, (335, 55))

			text = SUBTITLE_FONT.render("YOUR MODE", 1, WHITE)
			self.screen.blit(text, (300, 100))

			pygame.display.update()


	def screen_controller(self) :

		while self.choosing_mode :

			for event in pygame.event.get() :

				if event.type == pygame.QUIT :
					self.running = False
					self.choosing_mode = False
					pygame.quit()

				elif event.type == pygame.MOUSEBUTTONDOWN :
					self.check_mouse(event.pos)


	def choose_mode(self) :

		intro.play()

		# Create new threads
		thread_1 = threading.Thread(target = self.draw_screen, name="screen")
		thread_2 = threading.Thread(target = self.screen_controller, name="mouse")

		# Start threads
		thread_1.start()
		thread_2.start()

		start = self.screen_controller()

		# Wait for all threads to end
		while self.choosing_mode :
			thread_1.join()
			thread_2.join()


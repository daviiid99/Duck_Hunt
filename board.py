from resources import *
import threading
import json
import random
import time
from datetime import date
from datetime import datetime

class Board :

	def __init__(self) :
		pygame.init()
		self.running = True
		self.clock = pygame.time.Clock()
		self.screen = WIN
		self.screen_rect = self.screen.get_rect()
		self.playing = True
		self.duck_x = 0
		self.duck_y = 300
		self.duck_rect = pygame.Rect(self.duck_x, self.duck_y, 60, 60) # Variable rect for ducks on display

		self.shots = 3 # Max number of shots for one duck
		self.remaining_shots_img = [zero_shot, one_shot , two_shots, all_shots]
		self.current_shots_img = self.remaining_shots_img[self.shots]

		self.dog_animation = True
		self.dog_animations_list = [walking_1, walking_2, walking_3, walking_4, walking_5, walking_6, jump_1, jump_2, jump_3]
		self.current_dog_animation = walking_1
		self.current_dog_x = 50
		self.current_dog_y = 270

		self.game_ducks = 10 # Max number on ducks in one round
		self.shot_ducks = 0 # Fall ducks // Index of self.hits_img_list
		self.hits_img_list = [hit_zero, hit_one, hit_two, hit_three, hit_four, hit_five, hit_six, hit_seven, hit_eight, hit_nine, hit_ten]
		self.current_hits_img = self.hits_img_list[self.shot_ducks] # Current img at given index


		self.current_round = 1
		self.ducks_available = ["blue", "green", "brown"]

		self.current_score = 000000

		self.round_animation = True

		self.current_duck_img = blue_horizontal_1
		self.current_vel_x = 0
		self.current_vel_y = 0

		self.current_duck_color = ""

		self.isFlying = False
		self.location = 0
		self.isFalling = False

		self.brown_duck_falling = [brown_falling_1, brown_falling_2, brown_falling_3, brown_falling_4]
		self.blue_duck_falling = [blue_falling_1, blue_falling_2, blue_falling_3, blue_falling_4]
		self.green_duck_falling = [green_falling_1, green_falling_2, green_falling_3, green_falling_4]


	def draw_board(self) :

		while self.playing : 

			# Draw background
			now = datetime.now()
			hora = now.strftime("%H")

			if hora < "20" and hora >="10" :
				self.screen.blit(board_day_bg, (0,0))

			else :
				self.screen.blit(board_night_bg, (0,0))

			if self.shots == 1 :

				if hora < "20" and hora >="10" :
					self.screen.blit(board_day_blood_bg, (0,0))

				else :
					self.screen.blit(board_night_blood_bg, (0,0))


			# Draw remaining ducks on display
			self.screen.blit(self.current_hits_img, (240, 465))

			# Draw remaining shots on display
			self.screen.blit(self.current_shots_img, (95, 468))


			# Draw initial dog animation
			if self.dog_animation :
				self.screen.blit(self.current_dog_animation, (self.current_dog_x, self.current_dog_y))

			# Draw Current round
			ronda = SMALLEST_FONT.render("R=" + str(self.current_round), 1, YELLOW)
			self.screen.blit(ronda, (105, 425))

			# Draw Current score
			score = SMALLEST_FONT.render(str(self.current_score), 1, WHITE)
			self.screen.blit(score, (650, 460))

			score = SMALLEST_FONT.render("SCORE", 1, WHITE)
			self.screen.blit(score, (730, 475))

			# Draw new round message
			if self.round_animation :

				self.screen.blit(round, (260, 40))

				round_text = SUBTITLE_FONT.render("ROUND", 1, WHITE)
				self.screen.blit(round_text, (350, 55))

				round_text = SUBTITLE_FONT.render(str(self.current_round), 1, WHITE)
				self.screen.blit(round_text, (410, 100))

			# Duck on display

			if self.isFlying :
				self.screen.blit(self.current_duck_img, (self.duck_rect.x, self.duck_rect.y))

			# Game based mouse
			pygame.mouse.set_visible(False)
			self.screen.blit(cursor, ( pygame.mouse.get_pos() ))

			pygame.display.update()

	def shots_counter(self) :

		# Check remaining shots

		if self.shots > 0 :
			self.shots -=1

			if self.shots == 0 :
				if self.current_round < 10 :
					self.shots = 3
					self.current_round +=1

			self.current_shots_img = self.remaining_shots_img[self.shots]


	def check_ducks_impact(self, mouse) :

		if self.screen_rect.collidepoint(mouse) :
			gun_shot.play()
			self.shots_counter()

		if self.duck_rect.collidepoint(mouse) :
			self.isFalling = True


	def random_duck_location (self) :
		location = random.randint(200, 700)

		return location

	def generate_duck(self) :


		print(2)

		if not self.isFlying and not self.dog_animation :

			# Generate a randon duck color
			choose_duck = random.choice(self.ducks_available)

			# Save duck color into a variable
			self.current_duck_color = choose_duck

			# Assign duck sprite

			if choose_duck == "blue" :
				self.current_duck_img = blue_up_1

			elif choose_duck == "green" :
				self.current_duck_img = green_up_1

			elif choose_duck == "brown" :
				self.current_duck_img = brown_up_1


			# Generate random initial location
			self.location = self.random_duck_location()

			# Show current duck on display
			self.isFlying = True



	def shot_animation(self) :

		if self.current_duck_color == "blue" :
			self.current_duck_img = blue_shoot


	def duck_movement(self) :

		if self.isFlying :

			# Normal movement
			if self.shots == 3 :	
				self.duck_rect.x = self.location
				self.duck_rect.y -=5
				self.clock.tick(15)

			elif self.shots == 2 and not self.isFalling:
				self.duck_rect.x += 5
				self.clock.tick(15)


			elif self.shots == 0 or self.shots == 1 or self.shots == 2 and self.isFalling :
				self.shot_animation()
				clock.tick(5)
				self.falling_animation()

	def draw_fall(self) :

		if self.current_duck_color == "blue" :
			while self.duck_rect.y < 300 :
				for duck in self.blue_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)

			self.isFlying = False
			falling.stop()


		elif self.current_duck_color == "green" :
			while self.duck_rect.y < 300 :
				for duck in self.green_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)

			self.isFlying = False
			falling.stop()


		elif self.current_duck_color == "brown" :
			while self.duck_rect.y < 300 :
				for duck in self.brown_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)

			self.isFlying = False
			falling.stop()


	def falling_animation(self) :

		falling.play()
		self.draw_fall()
	
	def flying_ducks (self) :

		while self.playing :
			self.generate_duck()
			self.duck_movement()


	def board_controller(self) :

		while self.playing :

			for event in pygame.event.get() :

				if event.type == pygame.QUIT :
					self.running = False
					self.playing = False
					pygame.quit()

				elif event.type == pygame.MOUSEBUTTONDOWN :
					self.check_ducks_impact(event.pos)


	def initial_dog_animation (self) :
		
		count = 0
		count_animation = 0

		while self.dog_animation :

			while count < 5 :
				self.current_dog_animation = self.dog_animations_list[count_animation]

				if count_animation != 5 :
					self.current_dog_x += 6

				if count_animation == 7 :
					self.current_dog_y +=20
					clock.tick(30)
					count +=1

				else :
					clock.tick(5)
					count +=1

				if count_animation == 6 :
					self.round_animation = False
					dog_bark.play()
					self.current_dog_y -=30
					clock.tick(30)


				if count == 4 :
					if count_animation < 8 :
						count_animation +=1
					count = 0

				if count_animation >= 8 :
					self.dog_animation = False


	def start_game(self) :

		# Create new threads

		thread_1 = threading.Thread(target=self.draw_board, name="ui")
		thread_2 = threading.Thread(target = self.board_controller, name="controller")
		thread_3 = threading.Thread(target= self.initial_dog_animation, name="dog anim")
		thread_4 = threading.Thread(target= self.flying_ducks, name="duck")

		# Start threads
		thread_1.start()
		thread_3.start()
		thread_4.start()
		thread_2.start()

		start = self.board_controller()

		# Wait for all threads to end
		while self.playing :
			thread_3.join()
			thread_4.join()
			thread_1.join()
			thread_2.join()
			
			

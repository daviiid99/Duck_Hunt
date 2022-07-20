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
		self.is_free = False

		self.brown_duck_falling = [brown_falling_1, brown_falling_2, brown_falling_3, brown_falling_4]
		self.blue_duck_falling = [blue_falling_1, blue_falling_2, blue_falling_3, blue_falling_4]
		self.green_duck_falling = [green_falling_1, green_falling_2, green_falling_3, green_falling_4]

		self.blue_duck_flying_right = [blue_up_1_right, blue_up_2_right, blue_up_3_right]
		self.blue_duck_flying_left = [blue_up_1_left, blue_up_2_left, blue_up_3_left]

		self.brown_duck_flying_right = [brown_up_1_right, brown_up_2_right, brown_up_3_right]
		self.brown_duck_flying_left = [brown_up_1_left, brown_up_2_left, brown_up_3_left]

		self.green_duck_flying_right = [green_up_1_right, green_up_2_right, green_up_3_right]
		self.green_duck_flying_left = [green_up_1_left, green_up_2_left, green_up_3_left]

		self.eureka = False


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

			# Draw capture
			if self.eureka :
				self.screen.blit(one_duck, (self.duck_rect.x , self.duck_rect.y))

			# Game based mouse
			pygame.mouse.set_visible(False)
			self.screen.blit(cursor, ( pygame.mouse.get_pos() ))

			pygame.display.update()

	def shots_counter(self) :

		# Check remaining shots

		if self.shots > 0 :
			self.shots -=1
			self.current_shots_img = self.remaining_shots_img[self.shots]

			if self.shots == 0:

				if self.current_round < self.game_ducks :
					self.current_round +=1


	def refresh_remaining_ducks(self) :

		# Just Increasing the variable doesn't seem to work properly
		self.shot_ducks +=1
		self.current_hits_img = self.hits_img_list[self.shot_ducks] 


	def refresh_remaining_shots(self) :

		# Just Increasing the variable doesn't seem to work properly
		self.shots = 3
		self.current_shots_img = self.remaining_shots_img[self.shots]


	def check_ducks_impact(self, mouse) :

		if self.screen_rect.collidepoint(mouse) :
			gun_shot.play()
			self.shots_counter()

		if self.duck_rect.collidepoint(mouse) :
			self.isFalling = True
			self.shots_counter()


	def shot_duck_update(self) :

		# Increase player score
		self.increase_counter()

		# Update remaining ducks
		self.refresh_remaining_ducks()

		# Remove current duck from the total
		self.remove_duck()


	def increase_counter(self) :
		# Counter will increase dependant of the duck color

		if self.current_duck_color == "blue" :
			self.current_score +=1000

		elif self.current_duck_color == "green" :
			self.current_score += 1500

		elif self.current_duck_color == "brown" :
			self.current_score += 1500


	def random_duck_location (self) :
		location = random.randint(200, 700)

		return location

	def generate_duck(self) :

		if not self.isFlying :

			# Generate a randon duck color
			choose_duck = random.choice(self.ducks_available)

			# Save duck color into a variable
			self.current_duck_color = choose_duck

			# Assign duck sprite

			if choose_duck == "blue" :
				self.current_duck_img = blue_up_1_left

			elif choose_duck == "green" :
				self.current_duck_img = green_up_1_left

			elif choose_duck == "brown" :
				self.current_duck_img = brown_up_1_left

			# Generate random initial location
			self.location = self.random_duck_location()

			# Show current duck on display
			self.isFlying = True

	def shot_animation(self) :

		if self.current_duck_color == "blue" :
			self.current_duck_img = blue_shoot

		elif self.current_duck_color == "green" :
			self.current_duck_img = green_shoot

		elif self.current_duck_color == "brown" :
			self.current_duck_img = brown_shoot

	def remove_duck(self) :

		# Remove a duck from the total
		if self.is_free :
			self.game_ducks -=1

		self.is_free = False


	def choose_flying_duck(self, pos) :

		# Empty array

		duck = []

		if self.current_duck_color == "blue" :

			if pos == "left":
				duck = self.blue_duck_flying_left

			else :
				duck = self.blue_duck_flying_right


		elif self.current_duck_color == "green" :

			if pos == "left":
				duck = self.green_duck_flying_left

			else :
				duck = self.green_duck_flying_right


		elif self.current_duck_color == "brown" :

			if pos == "left":
				duck = self.brown_duck_flying_left

			else :
				duck = self.brown_duck_flying_right

		return duck

	def random_number(self) :

		number = random.randint(0, 99)

		return number

	def duck_movement(self) :

		if self.isFlying :

			# Normal movement
			self.duck_rect.x = self.location
			self.duck_rect.y = 300
			

			if self.shots >= 0   :	
				while self.duck_rect.y > 0 and not self.isFalling :
					count = 0

					if count == 0 : 
						number = self.random_number()

					if count == 10 :
						count = 0

					while number % 2 == 0 and not self.isFalling :
						# Choose duck assets pos
						duck_assets = self.choose_flying_duck("right")

						# Iterate with the new assets
						for ducks in duck_assets :

							# Assign the duck asset
							self.current_duck_img = ducks

							# Move the duck to the right
							self.duck_rect.y -= 5
							self.duck_rect.x += 5
							clock.tick(20)

							# Increase the counter
							count +=1

							# Check if the number is valid for this pos

							if count == 10 :
								count = 0

							if count == 0 : 
								number = self.random_number()

					while number % 2 == 1 and not self.isFalling:

						# Choose duck assets pos
						duck_assets = self.choose_flying_duck("left")

						# Iterate with the new assets
						for ducks in duck_assets :

							# Assign the duck asset
							self.current_duck_img = ducks

							# Move the duck to the right
							self.duck_rect.y -= 5
							self.duck_rect.x -= 5
							clock.tick(20)

							# Increase the counter
							count +=1

							# Check if the number is valid for this pos

							if count == 10 :
								count = 0

							if count == 0 : 
								number = self.random_number()



				if self.duck_rect.y == 0 and not self.isFalling:
					while self.duck_rect.y < 300 and not self.isFalling :
						count = 0
						for duck in duck_assets :

							if count == 10 :
								count = 0

							if count == 0 : 
								number = self.random_number()

							self.current_duck_img = duck
							self.duck_rect.y += 5

							if number % 2 == 0 :
								self.duck_rect.x -= 5
								clock.tick(20)

							else :
								self.duck_rect.x += 5
								self.clock.tick(20)

							count +=1

				if self.shots == 0 and not self.isFalling:
					self.isFlying = False

		if self.isFalling :
			self.shot_animation()
			clock.tick(5)
			self.falling_animation()
			self.eureka_time()
			self.refresh_remaining_shots()
			self.shot_duck_update()

	def eureka_time(self) :
		self.eureka = True
		show.play()
		count = 0

		while count < 5 :
			self.clock.tick(5)
			count +=1

		self.eureka = False

	def draw_fall(self) :

		if self.current_duck_color == "blue" :
			while self.duck_rect.y < 300 :
				for duck in self.blue_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)


		elif self.current_duck_color == "green" :
			while self.duck_rect.y < 300 :
				for duck in self.green_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)


		elif self.current_duck_color == "brown" :
			while self.duck_rect.y < 300 :
				for duck in self.brown_duck_falling :
					self.current_duck_img = duck
					self.duck_rect.y += 5
					self.clock.tick(30)


	def falling_animation(self) :

		falling.play()
		self.draw_fall()
		lands.play()
		self.isFlying = False
		self.isFalling = False
		falling.stop()
	
	def flying_ducks (self) :

		while self.playing :
			if not self.dog_animation :
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
			
			

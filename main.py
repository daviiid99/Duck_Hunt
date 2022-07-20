from resources import *
from modes import *
import threading

vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

class Main :

	def __init__(self) :
		pygame.init()
		self.running = True
		self.clock = pygame.time.Clock()
		self.screen = WIN
		self.mouse = vec()
		self.screen_rect = self.screen.get_rect()
		self.press_to_start = True
		self.count = 0


	def draw_title_screen(self) :

		while self.press_to_start :

			dog_x = 50
			duck_x = dog_x
			duck_y = 250
			dog_jump = 400
			count = 0

			# Dog walking // Duck flying

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_1, blue_horizontal_1, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 50
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_2, blue_horizontal_1, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 55
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_3, blue_horizontal_3, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 60
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_4, blue_horizontal_3, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 65
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_5, blue_horizontal_1, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 70
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_6, blue_horizontal_2, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 0
					duck_x = dog_x + 75
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(walking_6, blue_horizontal_2, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 0
					duck_x = dog_x + 80
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(jump_1, blue_up_1_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 85
					duck_y -= 10
					dog_jump  -= 10
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(jump_1, blue_up_2_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(10)
					dog_x += 10
					duck_x = dog_x + 90
					duck_y -= 10
					dog_jump  -= 10
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(jump_1, blue_up_1_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(30)
					dog_x += 10
					duck_x = dog_x + 95
					duck_y -= 10
					dog_jump  -= 10
					count +=1

			count = self.count

			while count < 5  :

				if self.press_to_start :

					self.draw(jump_1, blue_up_2_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(30)
					dog_x += 10
					duck_x = dog_x + 100
					duck_y -= 10
					dog_jump  -= 10
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(jump_2, blue_up_2_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(30)
					dog_x += 10
					duck_x = dog_x + 105
					duck_y -= 10
					dog_jump += 20
					count +=1

			count = self.count

			while count < 5 :

				if self.press_to_start :

					self.draw(jump_2, blue_up_3_right, dog_x, duck_x, duck_y, dog_jump)
					self.clock.tick(30)
					dog_x += 10
					duck_x = dog_x + 110
					duck_y -= 10
					dog_jump += 20
					count +=1

		
	def draw(self, dog, duck, dog_x, duck_x, duck_y, dog_jump) :
		# Set background
		self.screen.blit(title_screen_bg, (0,0))

		# Title message
		text = TITLE_FONT.render("Press to Start", 1, WHITE)
		self.screen.blit(text, (270, 300))

		# Draw dog
		self.screen.blit(dog, (dog_x, dog_jump))

		# Draw duck
		self.screen.blit(duck, (duck_x, duck_y))

		pygame.display.update()


	def control_title_screen(self) :

		while self.press_to_start : 

			for event in pygame.event.get() :
				if event.type == pygame.QUIT :
					self.running = False
					self.press_to_start = False
					pygame.quit()
					

				elif event.type == pygame.MOUSEBUTTONDOWN :
					self.check_mouse(event.pos)

	def check_mouse(self, mouse) :
		if self.screen_rect.collidepoint(mouse) :
			self.running = False
			self.press_to_start = False
			title.stop()
			modes = Mode()
			modes.choose_mode()

	def play_music(self) :

		title.play()


	def start_title_screen(self) :

		# Create new threads for title screen control
		thread_1 = threading.Thread(target = self.draw_title_screen, name="ui")
		thread_2 = threading.Thread(target = self.control_title_screen, name="mouse")
		thread_3 = threading.Thread(target = self.play_music, name="sound")

		# Start threads
		thread_1.start()
		thread_2.start()
		thread_3.start()

		# Wait for all threads to end
		start = self.control_title_screen()

		while self.press_to_start :
			thread_1.join()
			thread_2.join()
			thread_3.join()




main = Main()
main.start_title_screen()

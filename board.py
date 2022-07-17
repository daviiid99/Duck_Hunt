from resources import *
import threading
import json
import time

class Board :

	def __init__(self) :
		pygame.init()
		self.running = True
		self.clock = pygame.time.Clock()
		self.screen = WIN



	

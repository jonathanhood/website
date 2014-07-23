"""
pong.py, v1.0
A pong clone by Jonathan Hood
"""

import os, sys, random
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'

class Ball:
	def __init__(self, parent, color):
		self.parent = parent
		self.color = color
		
		#Set random start velocities
		random.seed()
		self.yvel = 1
		self.xvel = 1
		if random.randint(0, 1): self.yvel *= -1
		if random.randint(0, 1): self.xvel *= -1
		
		#Set initial position
		self.parentRect = self.parent.screen.get_rect()
		self.rect = Rect( self.parentRect.right / 2 - 10, self.parentRect.bottom / 2 - 40, 10, 10)
		
	def reset(self):
		#Reset inital position
		self.parentRect = self.parent.screen.get_rect()
		self.rect = Rect( self.parentRect.right / 2 - 10, self.parentRect.bottom / 2 - 40, 10, 10)
		
		#Reset initial velocity
		self.yvel = 1
		self.xvel = 1
		if random.randint(0, 1): self.yvel *= -1
		if random.randint(0, 1): self.xvel *= -1
		
	def move(self):
		self.rect.move_ip(self.xvel, self.yvel)
		
		if self.yvel >= 0: #Moving Downward
			if self.rect.bottom < self.parentRect.bottom -1:
				self.rect.move_ip(0, self.yvel)
			else:
				self.yvel *= -1
		else: #Moving upward
			if self.rect.y > 1:
				self.rect.move_ip(0, self.yvel)
			else:
				self.yvel *= -1
		
		if self.xvel >= 0: #Moving Right
			if self.rect.right < self.parentRect.right-1:
				self.rect.move_ip(self.xvel, 0)
			else: #Player score
				self.parent.playerScore+=1
				self.parent.reset()
		else: #Moving Left
			if self.rect.x > 1:
				self.rect.move_ip(self.xvel, 0)
			else: #Comp Score
				self.parent.compScore+=1
				self.parent.reset()
		
	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)

class Paddle:
	def __init__(self, parent, color, x):
		self.parent = parent
		self.color = color
		
		#Set initial position
		self.rect = Rect(x-5, self.parent.screen.get_rect().bottom/2-40,20,80)
		
	def reset(self):
		#Reset initial position
		self.rect = Rect(self.rect.x, self.parent.screen.get_rect().bottom/2-40,20,80)
		
	def move(self):
		keys = pygame.key.get_pressed()
		if keys[K_UP]:
			if self.rect.y > 1:
				self.rect.move_ip(0,-5)
		if keys[K_DOWN]:
			if self.rect.bottom < self.parent.screen.get_rect().bottom - 1:
				self.rect.move_ip(0,5)
				
		#Do Collision Detect, Adjust velocity and Position accordingly
		if self.rect.colliderect(self.parent.ball.rect):
			if self.parent.ball.xvel < 0:
				self.parent.ball.rect.x = self.rect.right + 1
				self.parent.ball.xvel += random.randint(-1, 0)
			else:
				self.parent.ball.rect.x = self.rect.x - self.parent.ball.rect.width - 1
				self.parent.ball.xvel += random.randint(0,1)
				
			if self.parent.ball.yvel > 0:
				self.parent.ball.yvel += random.randint(0,1)
			else:
				self.parent.ball.yvel += random.randint(-1, 0)
				
			self.parent.ball.xvel *= -1
			
	def draw(self, screen):
		pygame.draw.rect(screen,self.color,self.rect)
		
class AIPaddle(Paddle):
	def __init__(self, parent, color, x, level):
		self.level = level
		self.calcdone = 0
		
		self.parent = parent
		self.color = color
		
		#Set initial position
		self.rect = Rect(x-5, self.parent.screen.get_rect().bottom/2-40,20,80)
		
	def move(self):
		ballRect = Rect(self.parent.ball.rect.x, self.parent.ball.rect.y, self.parent.ball.rect.width, self.parent.ball.rect.height)
		ballxvel = self.parent.ball.xvel
		ballyvel = self.parent.ball.yvel
		parentRect = self.parent.screen.get_rect()
		
		#Check if the ball is moving towards me
		x1 = ballRect.x
		x2 = ballRect.x + ballxvel
		dif1 = abs(self.rect.x - x1)
		dif2 = abs(self.rect.x - x2)

		if(dif1 > dif2): #If the ball is moving towards me, react
			if ballRect.y > self.rect.y + 40: #Downward move required
				if self.rect.bottom < parentRect.bottom - 1:
					self.rect.move_ip(0, 5)
						
			if ballRect.y < self.rect.y + 40: #Upward move required
				if self.rect.y > 1:
					self.rect.move_ip(0, -5)
		
		#Do Collision Detect, Adjust ball Velocity and Position accordingly
		if self.rect.colliderect(self.parent.ball.rect):
			if self.parent.ball.xvel < 0:
				self.parent.ball.rect.x = self.rect.right + 1
				self.parent.ball.xvel += random.randint(-1, 0)
			else:
				self.parent.ball.rect.x = self.rect.x - self.parent.ball.rect.width - 1
				self.parent.ball.xvel += random.randint(0,1)
				
			if self.parent.ball.yvel > 0:
				self.parent.ball.yvel += random.randint(0,1)
			else:
				self.parent.ball.yvel += random.randint(-1, 0)
				
			self.parent.ball.xvel *= -1
	
class Pong:
	def __init__(self):
		#Init Vars
		self.play = 0
		self.playerScore = 0
		self.compScore = 0
	
		#Init pygame
		pygame.init()	#Do initial init
		self.screen = pygame.display.set_mode((640, 480)) #Open a window, then get a handle to it
		pygame.display.set_caption('PyPong') #Set our window caption
		pygame.mouse.set_visible(1) #Set to one to show mouse while in window
		
		#Init font
		self.font = pygame.font.Font(None, 34)
		
		#Init objects
		self.clock = pygame.time.Clock()
		self.player = Paddle(self, (0, 255, 0), 20)
		self.ball = Ball(self, (255, 255, 255))
		self.comp = AIPaddle(self, (0, 0, 255), 600, 200)

		#Create a solid background color
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0, 0, 0))
		
	def reset(self):
		#Check for end of game condition
		if self.playerScore == 10 or self.compScore == 10:
			self.play = 0
		
		#Reset the ball
		self.ball.reset()
	
	def updateText(self):
		self.text = self.font.render(str(self.playerScore) + ' - ' + str(self.compScore), True, (255,255, 255), (0, 0, 0))
		self.textRect = self.text.get_rect()
		self.textRect.centerx = self.screen.get_rect().centerx
		self.textRect.y = 0
		self.screen.blit(self.text, self.textRect)
		
	def menu(self):
		keys = pygame.key.get_pressed()
		if keys[K_RETURN]:
			self.play = 1
			showMenu = 0
		if keys[K_ESCAPE]:
			sys.exit(0)
			
		self.screen.blit(self.background, (0,0))
		
		title = self.font.render( "Welcome to PyPong", True, (255,255,255), (0,0,0))
		titleRect = title.get_rect()
		titleRect.centerx = self.screen.get_rect().centerx
		titleRect.y = 0
		self.screen.blit(title, titleRect)
		
		if(self.playerScore == 10):
			congrats = self.font.render( "Congratutalions, You Win!", True, (255, 255, 255), (0,0,0))
			congratsRect = congrats.get_rect()
			congratsRect.centerx = self.screen.get_rect().centerx
			congratsRect.centery = self.screen.get_rect().centery / 2
			self.screen.blit(congrats, congratsRect)
		elif(self.compScore == 10):
			lose = self.font.render( "You Lose, Try Again!", True, (255, 255, 255), (0,0,0))
			loseRect = lose.get_rect()
			loseRect.centerx = self.screen.get_rect().centerx
			loseRect.centery = self.screen.get_rect().centery / 2
			self.screen.blit(lose, loseRect)
		
		text = self.font.render( "Press Enter to play, ESC to leave", True, (255, 255, 255), (0,0,0))
		textRect = text.get_rect()
		textRect.centerx = self.screen.get_rect().centerx
		textRect.centery = self.screen.get_rect().centery
		self.screen.blit(text, textRect)
		
		pygame.display.flip()
		
	def game(self):
		#Update game objects
		self.player.move()
		self.comp.move()
		self.ball.move()
		
		#Update our screen
		self.screen.blit(self.background, (0,0))
		self.ball.draw(self.screen)
		self.player.draw(self.screen)
		self.comp.draw(self.screen)
		self.updateText()
		
	def run(self):
		while 1: #Game loop
			self.clock.tick(60) #Limit to 60fps
			
			for event in pygame.event.get(): #Handle SDL Events
				if event.type == QUIT: #Quit event thrown, leave program
					return
			
			#See if we need the menu
			if self.play != 1:
				self.menu()
			else: #Play Game
				self.game()
			
			#Flip our buffers
			pygame.display.flip()

#PROGRAM START
Pong().run()
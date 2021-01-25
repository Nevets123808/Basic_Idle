import pygame, math
import pygame_reg
from pygame.locals import *

pygame.init()

SCREENWIDTH = 640
SCREENHEIGHT =480

FIELD_WIDTH = 256
FIELD_HEIGHT = 32

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

clock = pygame.time.Clock()
class Unit:
	def __init__(self, name,value, basecost, speed, x,y):
		self.rect = pygame.Rect(x,y,FIELD_WIDTH*2,FIELD_HEIGHT*2)
		self.name = name
		self.value = value
		self.amount = 0
		self.basecost = basecost
		self.cost = basecost
		self.speed = speed
		self.nameBox = pygame_reg.InfoBox(x,y, FIELD_WIDTH, FIELD_HEIGHT, self.name, str(self.amount))
		self.costBox = pygame_reg.InfoBox(x,y+FIELD_HEIGHT, FIELD_WIDTH, FIELD_HEIGHT, "Cost",str(self.cost))

	def setcost(self):
		return int(self.cost*self.speed**self.amount)

	def update(self,GameData):
		GameData.money += self.value*self.amount

	def draw(self,screen):
		self.nameBox.valueBox.text = str(self.amount)
		self.costBox.valueBox.text = str(self.cost)
		self.nameBox.draw(screen)
		self.costBox.draw(screen)

	def eventHandler(self,event,gameData):
		if event.type == MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				if self.cost < gameData.money:
					self.amount +=1
					gameData.money -= self.cost
					self.cost += self.setcost()
class GameData:
	def __init__(self):
		self.money = 11
		self.moneyBox = pygame_reg.InfoBox((SCREENWIDTH/2-FIELD_WIDTH), 10, FIELD_WIDTH,FIELD_HEIGHT, "Money", str(self.money))
	def draw(self,screen):
		self.moneyBox.valueBox.text = str(self.money)
		self.moneyBox.draw(screen)
def main():
	time = 0
	game = GameData()
	unit1 =Unit("Unit1", 1, 1, 1.1, 10,64)
	unit2 =Unit("Unit2", 2, 10, 1.2, 10, 128)
	units = [unit1, unit2]
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			for unit in units:
				unit.eventHandler(event,game)
		screen.fill((255,255,255))
		for unit in units:
			if time > 1000:
				unit.update(game)

				print("tick")
			unit.draw(screen)
		time %= 1000
		game.draw(screen)
		pygame.display.flip()
		clock.tick(30)
		time += clock.get_time()

	pygame.quit()

if __name__ == "__main__":
	main()


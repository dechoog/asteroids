import pygame
from constants import *
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(F"Screen height: {SCREEN_HEIGHT}")
	clock  = pygame.time.Clock()
	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		tp = clock.tick(60)
		dt = tp/1000
if __name__ == "__main__":
	main()

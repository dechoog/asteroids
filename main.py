import pygame
from circleshape import *
from player import *
from asteroid import *
from constants import *
from asteroidfield import *

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers=(updatable,drawable)
	Asteroid.containers=(asteroids,updatable,drawable)
	AsteroidField.containers=(updatable)
	Shot.containers=(shots,updatable,drawable)
	

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(F"Screen height: {SCREEN_HEIGHT}")
	clock  = pygame.time.Clock()
	dt = 0
	Player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	Asteroid1 = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0,0,0))

		for todraw in drawable:
			todraw.draw(screen)

		updatable.update(dt)

		for asteroid in asteroids:
			if Player1.collision(asteroid):
				print("Game Over")
				return
		
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()
				#algo
			
		#Player1.draw(screen)
		#Player1.update(dt)
		pygame.display.flip()
		tp = clock.tick(60)
		dt = tp/1000
		
if __name__ == "__main__":
	main()

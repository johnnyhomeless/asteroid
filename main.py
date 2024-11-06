import pygame
import sys
from constants import *
from circleshape import CircleShape
import player
from asteroidfield import AsteroidField
from asteroid import Asteroid 

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  
    AsteroidField.containers = (updatable,) 
    Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_instance = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        for x in updatable:
            x.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player_instance):
                print("Game over!")
                sys.exit()

        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
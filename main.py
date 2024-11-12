import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    sprites = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group() 

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
   
    sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        sprites.update(dt)
        asteroidfield.update(dt)

        screen.fill((0, 0, 0))
        sprites.draw(screen)
        asteroidfield.asteroids.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
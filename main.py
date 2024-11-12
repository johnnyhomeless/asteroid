import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Set up the font
    game_over_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 74)  # None uses default font, 74 is size
    game_over_text = game_over_font.render('Game Over!', True, (255, 255, 255))  # Red text
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    sprites = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
   
    sprites.add(player)

    running = True
    game_over = False  # New flag to track game over state
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        if not game_over:
            sprites.update(dt)
            asteroidfield.update(dt)
    
        for asteroid in asteroidfield.asteroids:
             if player.collision(asteroid):
                 print("Game over!")
                 game_over = True

        screen.fill((0, 0, 0))
        sprites.draw(screen)
        asteroidfield.asteroids.draw(screen)

        if game_over:
            screen.blit(game_over_text, game_over_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False
        else:
            pygame.display.flip()     

        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
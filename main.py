import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from text_manager import TextManager
import sys

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    FIXED_DT = 1/60 
    clock = pygame.time.Clock()
    #  dt = 0

    text_manager = TextManager()
    sprites = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
   
    sprites.add(player)

    running = True
    game_over = False
    show_start_message = True
    show_logo = True
    space_just_pressed = False

    while running:
        dt = FIXED_DT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if show_start_message:
                    show_start_message = False
                    show_logo = False
                    space_just_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    space_just_pressed = False

        if not game_over and not show_start_message and not space_just_pressed:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                new_shot = player.shoot()
                if new_shot:
                    shots.add(new_shot)

        if not game_over and not show_start_message:
            sprites.update(dt)
            asteroidfield.update(dt)
            shots.update(dt)

        for asteroid in asteroidfield.asteroids:
            if player.collision(asteroid):
                print("Game over!")
                game_over = True

        screen.fill((0, 0, 0))

        if show_start_message:
            text_manager.update_start_message(dt)

        if not game_over and not show_start_message:
            sprites.draw(screen)
            asteroidfield.asteroids.draw(screen)
            shots.draw(screen)
        
        text_manager.draw(screen, show_logo, show_start_message, game_over)

        if game_over:
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        pygame.display.flip()   
        clock.tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()
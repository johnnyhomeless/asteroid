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
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    # Load the logo font
    logo_font = pygame.font.Font("fonts/INVASION2000.TTF", 96)
    logo_text = logo_font.render("AstroCazzo", True, (255, 255, 255))
    logo_rect = logo_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

    game_over_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 74)
    game_over_text = game_over_font.render('Game Over!', True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    sprites = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
   
    sprites.add(player)

    running = True
    game_over = False
    show_start_message = True
    show_logo = True
    start_message_visible = True
    start_message_timer = 0.5  # Time (in seconds) to show/hide the start message

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_start_message = False
                show_logo = False

        if not game_over and not show_start_message:
            sprites.update(dt)
            asteroidfield.update(dt)
    
        for asteroid in asteroidfield.asteroids:
             if player.collision(asteroid):
                 print("Game over!")
                 game_over = True

        screen.fill((0, 0, 0))
        if show_logo:
            screen.blit(logo_text, logo_rect)

        if show_start_message:
            start_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 36)
            if start_message_visible:
                start_text = start_font.render("Press SPACE to start", True, (255, 255, 255))
            else:
                start_text = start_font.render("Press SPACE to start", True, (0, 0, 0))  # Make the text invisible
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 100))
            screen.blit(start_text, start_rect)

            start_message_timer -= dt
            if start_message_timer <= 0:
                start_message_visible = not start_message_visible
                start_message_timer = 0.5

        if not game_over and not show_start_message:
            sprites.draw(screen)
            asteroidfield.asteroids.draw(screen)
        elif game_over:
            screen.blit(game_over_text, game_over_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        pygame.display.flip()     

        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
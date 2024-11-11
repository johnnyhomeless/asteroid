import pygame
from constants import *
from  player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Set up sprite groups
    sprites = pygame.sprite.Group()
    
    # Create player and add to sprite group
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    sprites.add(player)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Update
        sprites.update(dt)

        # Draw
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        pygame.display.flip()

        # Update timing
        dt = clock.tick(60) / 1000.0

    pygame.quit()

if __name__ == "__main__":
    main()
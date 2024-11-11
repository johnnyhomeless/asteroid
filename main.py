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

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    while True:
       
        updatable.update()
        pygame.Surface.fill(screen, (0, 0, 0))
        drawable.draw(screen)
        pygame.display.flip()

        new_dt = clock.tick(60)
        dt = new_dt / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return





if __name__ == "__main__":
    main()
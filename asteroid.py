import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))

    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

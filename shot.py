# shot.py
from constants import SHOT_RADIUS
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize with the shot radius
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
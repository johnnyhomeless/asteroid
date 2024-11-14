import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        initial_speed = 2
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * initial_speed
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))

    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []

        offset = self.radius * 0.5
        positions = [
            self.position + pygame.Vector2(offset, 0),
            self.position + pygame.Vector2(-offset, 0),
        ]
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroids = []

        rand_angle = random.uniform(20, 51)
        for i, pos in enumerate(positions):
            angle = rand_angle if i == 0 else -rand_angle
            new_asteroid = Asteroid(pos.x, pos.y, new_radius)
            new_asteroid.velocity = self.velocity.rotate(angle) * 1.5
            new_asteroids.append(new_asteroid)
        
        self.kill()
        return new_asteroids
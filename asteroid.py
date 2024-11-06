import pygame
from circleshape import CircleShape
from pygame.math import Vector2
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = Vector2(0, 0)  
     
     
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

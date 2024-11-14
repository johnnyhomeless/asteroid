import pygame
from circleshape import CircleShape
from constants import (SHOT_RADIUS,
                      PLAYER_SHOOT_SPEED)

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        
        self.velocity = pygame.Vector2(direction)
        self.velocity.scale_to_length(PLAYER_SHOOT_SPEED)
        
        # Create sprite image
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 4, 4))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        # Optional: If you want to implement custom drawing
        pygame.draw.circle(screen, (255, 255, 255), 
                         self.position, self.radius)
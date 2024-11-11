import pygame
from circleshape import CircleShape
from constants import (PLAYER_RADIUS,
                      PLAYER_TURN_SPEED,
                      PLAYER_SPEED,
                      SCREEN_WIDTH,
                      SCREEN_HEIGHT)

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        
        # Create the image surface
        self.image = pygame.Surface((PLAYER_RADIUS * 3, PLAYER_RADIUS * 3), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.update_sprite()

    def triangle(self):
        # Calculate triangle points relative to sprite surface center
        center = pygame.Vector2(self.image.get_width() / 2, self.image.get_height() / 2)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]

    def update_sprite(self):
        # Clear the surface
        self.image.fill((0, 0, 0, 0))
        # Draw the triangle on the surface
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)
        # Update rect position
        self.rect.center = self.position

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.update_sprite()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(dt * -1)
         
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
         
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0 
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT

        # Update the sprite's position
        self.update_sprite()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
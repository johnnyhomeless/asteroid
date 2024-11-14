import pygame
from constants import *

class TextManager:
    def __init__(self):
        # Load fonts
        self.logo_font = pygame.font.Font("fonts/INVASION2000.TTF", 96)
        self.game_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 74)
        self.start_font = pygame.font.Font("fonts/ARCADECLASSIC.TTF", 36)

        # Create text surfaces
        self.logo_text = self.logo_font.render("AstroCazzo", True, (255, 255, 255))
        self.logo_rect = self.logo_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

        self.game_over_text = self.game_font.render('Game Over!', True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        # Start message state
        self.start_message_visible = True
        self.start_message_timer = 0.5
        self.start_text_visible = self.start_font.render("Press SPACE to start", True, (255, 255, 255))
        self.start_text_invisible = self.start_font.render("Press SPACE to start", True, (0, 0, 0))
        self.start_rect = self.start_text_visible.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 100))

    def update_start_message(self, dt):
        self.start_message_timer -= dt
        if self.start_message_timer <= 0:
            self.start_message_visible = not self.start_message_visible
            self.start_message_timer = 0.5

    def draw(self, screen, show_logo=False, show_start_message=False, game_over=False):
        if show_logo:
            screen.blit(self.logo_text, self.logo_rect)

        if show_start_message:
            start_text = self.start_text_visible if self.start_message_visible else self.start_text_invisible
            screen.blit(start_text, self.start_rect)

        if game_over:
            screen.blit(self.game_over_text, self.game_over_rect)
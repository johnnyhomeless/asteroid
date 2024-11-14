import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from text_manager import TextManager
from score import Score
import sys

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    text_manager = TextManager()
    sprites = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    shots = pygame.sprite.Group()
    sprites.add(player)
    score = Score()

    return screen, text_manager, sprites, player, asteroidfield, shots, score

def handle_events(running, show_start_message, show_logo, space_just_pressed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if show_start_message:
                show_start_message = False
                show_logo = False
                space_just_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_just_pressed = False
    return running, show_start_message, show_logo, space_just_pressed

def handle_shooting(player, shots, game_over, show_start_message, space_just_pressed):
    if not game_over and not show_start_message and not space_just_pressed:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot:
                shots.add(new_shot)

def check_collisions(player, asteroidfield, shots, score):
    game_over = False
    for asteroid in list(asteroidfield.asteroids): 
        for bullet in shots:
            distance = bullet.position.distance_to(asteroid.position)
            if distance <= bullet.radius + asteroid.radius:
                bullet.kill()
                if asteroid.radius >= 40:
                    score.add_points(20)
                elif asteroid.radius >= 25:
                    score.add_points(50)
                else:
                    score.add_points(100)
                new_asteroids = asteroid.split()
                asteroidfield.asteroids.add(*new_asteroids)
       
        if player.collision(asteroid):
            print("Game over!")
            game_over = True
    return game_over

def update_game(sprites, asteroidfield, shots, dt):
    sprites.update(dt)
    asteroidfield.update(dt)
    shots.update(dt)

def draw_game(screen, sprites, asteroidfield, shots, text_manager, show_logo, show_start_message, game_over, dt, score):
    screen.fill((0, 0, 0))
    
    font = pygame.font.Font("fonts/INVASION2000.TTF", 20)
    score_text = font.render(f'Score: {score.points}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if show_start_message:
        text_manager.update_start_message(dt)
    
    if not game_over and not show_start_message:
        sprites.draw(screen)
        asteroidfield.asteroids.draw(screen)
        shots.draw(screen)
    
    text_manager.draw(screen, show_logo, show_start_message, game_over)

def main():
   screen, text_manager, sprites, player, asteroidfield, shots, score = init_game()
   
   clock = pygame.time.Clock()
   FIXED_DT = 1/60
   
   running = True
   game_over = False
   show_start_message = True
   show_logo = True
   space_just_pressed = False

   while running:
       dt = FIXED_DT
       
       running, show_start_message, show_logo, space_just_pressed = handle_events(
           running, show_start_message, show_logo, space_just_pressed)
       
       handle_shooting(player, shots, game_over, show_start_message, space_just_pressed)
       
       if not game_over and not show_start_message:
           update_game(sprites, asteroidfield, shots, dt)
       
       game_over = check_collisions(player, asteroidfield, shots, score)
       
       draw_game(screen, sprites, asteroidfield, shots, text_manager, 
                show_logo, show_start_message, game_over, dt, score)
       
       if game_over:
           pygame.display.flip()
           pygame.time.wait(2000)
           running = False

       pygame.display.flip()   
       clock.tick(60)  

   pygame.quit()

if __name__ == "__main__":
    main()
import pygame
from player import Player
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode([game_settings.screen_width, game_settings.screen_height])
    pygame.display.set_caption(game_settings.caption)
    
    player = Player(screen)

    while True:
        gf.check_events(player)
        player.update()
        gf.update_screen(game_settings, screen, player)
     
run_game()
import pygame
from player import Player
from settings import Settings
import game_functions as gf
from bubble import Bubble
###
def run_game():
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode([game_settings.screen_width, game_settings.screen_height])
    pygame.display.set_caption(game_settings.caption)
    
    player = Player(screen)
    
    bubbles = pygame.sprite.Group()

    while True:
        gf.check_events(game_settings, screen, player, bubbles)
        player.update()
        bubbles.update()
        gf.update_screen(game_settings, screen, player, bubbles)
     
run_game()
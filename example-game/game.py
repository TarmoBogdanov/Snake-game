import pygame
from player import Player
from button import Button
from settings import Settings
import game_functions as gf
from scoreboard import Scoreboard
from game_stats import GameStats
from bubble import Bubble
#
def run_game():
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode([game_settings.screen_width, game_settings.screen_height])
    pygame.display.set_caption(game_settings.caption)
    
    player = Player(screen)
    
    stats = GameStats()
    
    play_button = Button(game_settings, screen, "Play")
    
    sb = Scoreboard(game_settings, screen, stats)
    
    clock = pygame.time.Clock()
    
    bubbles = pygame.sprite.Group()
#
    while True:
        gf.check_events(game_settings, screen, player, bubbles, stats, play_button)
        if stats.game_active:    
            player.update()
            gf.update_bubbles(player, bubbles, stats, sb)
            bubbles.update()
        else:
            bubbles.empty()
        gf.update_screen(game_settings, screen, player, bubbles, clock, stats, play_button, sb)
     
run_game()
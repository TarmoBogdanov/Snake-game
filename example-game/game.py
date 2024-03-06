import pygame

from settings import Settings

def run_game():
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode([game_settings.screen_width, game_settings.screen_height])

    pygame.display.set_caption(game_settings.caption)

    running = True
    while running:
        screen.fill(game_settings.background_color)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        pygame.display.flip()
    pygame.quit()
    print(running)

run_game()

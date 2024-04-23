import pygame
import random

GRID_SIZE_X = 35
GRID_SIZE_Y = 35
GRID_WIDTH = 25
GRID_HEIGHT = 25

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE_X, GRID_HEIGHT * GRID_SIZE_Y))
running = True
#
snake = []

snake_direction = (1, 0)


snake.append((3, 3))

snake_length = 5

snake_growth = 2

apple_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = (-1, 0)
            if event.key == pygame.K_RIGHT:
                snake_direction = (1, 0)
            if event.key == pygame.K_DOWN:
                snake_direction = (0, 1)
            if event.key == pygame.K_UP:
                snake_direction = (0, -1)

    screen.fill((0, 0, 0))
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        running = False
    
    if new_head in snake:
        running = False

    snake.insert(0, new_head)
    
    if len(snake) >= snake_length:
        snake.pop()

    
    for piece in snake:
        pygame.draw.rect(screen, (0, 0, 255), (piece[0] * GRID_SIZE_X, piece[1] * GRID_SIZE_Y, GRID_SIZE_X, GRID_SIZE_Y))

    if snake[0] == apple_position:
        apple_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake_length += snake_growth
    
    pygame.draw.rect(screen, (255, 128, 0), (apple_position[0] * GRID_SIZE_X, apple_position[1] * GRID_SIZE_Y, GRID_SIZE_X, GRID_SIZE_Y))

    pygame.display.flip()

    clock.tick(7)
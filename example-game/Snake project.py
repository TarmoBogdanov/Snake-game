import pygame
import random
from Snake import Snake

GRID_SIZE_X = 35
GRID_SIZE_Y = 35
GRID_WIDTH = 25
GRID_HEIGHT = 25

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE_X, GRID_HEIGHT * GRID_SIZE_Y))
running = True

snake = Snake((3, 3), (1, 0), 5)
snake_growth = 2
apple_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
clock = pygame.time.Clock()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.direction = (-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = (1, 0)
            if event.key == pygame.K_DOWN:
                snake.direction = (0, 1)
            if event.key == pygame.K_UP:
                snake.direction = (0, -1)

    screen.fill((0, 0, 0))

    if not snake.move(GRID_WIDTH, GRID_HEIGHT):
        running = False
    
    for piece in snake.body:
        pygame.draw.rect(screen, (0, 0, 255), (piece[0] * GRID_SIZE_X, piece[1] * GRID_SIZE_Y, GRID_SIZE_X, GRID_SIZE_Y))

    if snake.body[0] == apple_position:
        apple_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        snake.length += snake_growth
    
    pygame.draw.rect(screen, (255, 128, 0), (apple_position[0] * GRID_SIZE_X, apple_position[1] * GRID_SIZE_Y, GRID_SIZE_X, GRID_SIZE_Y))

    pygame.display.flip()

    clock.tick(7)
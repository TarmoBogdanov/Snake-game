import pygame

class Snake:
    def __init__(self, initial_position, initial_direction, length):
        self.body = [initial_position]
        self.direction = initial_direction
        self.length = length

    def move(self, grid_width, grid_height):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        if new_head[0] < 0 or new_head[0] >= grid_width or new_head[1] < 0 or new_head[1] >= grid_height:
            return False
        
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        
        if len(self.body) >= self.length:
            self.body.pop()

        return True

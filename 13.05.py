import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        YELLOW = (255, 255, 0)
        screen.pygame.display.set_mode(size)
        for i in range(self.height + 1):
            pygame.draw.line(screen, YELLOW, [self.left, self.top + self.cell_size * i]
                             [self.left + self.cell_size * self.width, self.top + self.cell_size * i, 1])

    pygame.init()
    size = width, hei
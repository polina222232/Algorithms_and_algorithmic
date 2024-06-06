# main.py

import pygame
import sys

from Lines.conctasts import *
from board import Board


def main():
    pygame.init()
    size = BOARD_SIZE * CELL_SIZE + 2 * LEFT_MARGIN, BOARD_SIZE * CELL_SIZE + 3 * TOP_MARGIN
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lines")

    board = Board()
    board.set_view(LEFT_MARGIN, TOP_MARGIN, CELL_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill(BACKGROUND_COLOR)
        board.render(screen)
        pygame.display.flip()

        if all(all(cell != 0 for cell in row) for row in board.board):
            running = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

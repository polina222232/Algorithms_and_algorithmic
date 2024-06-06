# board.py

import pygame
import random
from Lines.conctasts import *


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.board = [[0] * self.size for _ in range(self.size)]
        self.left = LEFT_MARGIN
        self.top = TOP_MARGIN
        self.cell_size = CELL_SIZE
        self.selected = None
        self.next_balls = self.generate_next_balls()
        self.score = 0
        self.moves = 0
        self.error_message = ""
        self.generate_balls(NEW_BALLS)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                rect = pygame.Rect(self.left + col * self.cell_size,
                                   self.top + row * self.cell_size,
                                   self.cell_size, self.cell_size)
                pygame.draw.rect(screen, LINE_COLOR, rect, 1)
                ball = self.board[row][col]
                if ball:
                    pygame.draw.circle(screen, BALL_COLORS[ball - 1],
                                       rect.center, self.cell_size // 2 - 5)

        if self.selected:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(
                self.left + self.selected[1] * self.cell_size,
                self.top + self.selected[0] * self.cell_size,
                self.cell_size, self.cell_size), 3)

        # Render next balls
        for i, ball in enumerate(self.next_balls):
            pygame.draw.circle(screen, BALL_COLORS[ball - 1],
                               (self.left + (i + 0.5) * self.cell_size,
                                self.top - self.cell_size // 2),
                               self.cell_size // 2 - 5)

        # Render score and moves
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        moves_text = font.render(f"Moves: {self.moves}", True, (255, 255, 255))
        screen.blit(score_text, (self.left, self.top + self.size * self.cell_size + 10))
        screen.blit(moves_text, (self.left, self.top + self.size * self.cell_size + 40))

        # Render error message if any
        if self.error_message:
            error_text = font.render(self.error_message, True, (255, 0, 0))
            screen.blit(error_text, (self.left, self.top + self.size * self.cell_size + 70))
            self.error_message = ""

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x < self.left or y < self.top:
            return None
        col = (x - self.left) // self.cell_size
        row = (y - self.top) // self.cell_size
        if col >= self.size or row >= self.size:
            return None
        return row, col

    def on_click(self, cell_coords):
        if cell_coords:
            row, col = cell_coords
            if self.board[row][col]:
                self.selected = cell_coords
            elif self.selected and self.is_valid_move(self.selected, cell_coords):
                self.move_ball(self.selected, cell_coords)
                self.selected = None
                if not self.remove_lines():
                    self.generate_balls(NEW_BALLS)
                    self.moves += 1
            else:
                self.error_message = "Invalid move!"

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def generate_next_balls(self):
        return [random.randint(1, len(BALL_COLORS)) for _ in range(NEW_BALLS)]

    def generate_balls(self, count):
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if not self.board[r][c]]
        for ball in self.next_balls:
            if empty_cells:
                row, col = random.choice(empty_cells)
                self.board[row][col] = ball
                empty_cells.remove((row, col))
        self.next_balls = self.generate_next_balls()
        self.remove_lines()

    def is_valid_move(self, from_cell, to_cell):
        # Breadth-first search (BFS) to check for a valid path
        fr, fc = from_cell
        tr, tc = to_cell
        queue = [(fr, fc)]
        visited = set(queue)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.pop(0)
            if (r, c) == (tr, tc):
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size and (nr, nc) not in visited and self.board[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return False

    def move_ball(self, from_cell, to_cell):
        fr, fc = from_cell
        tr, tc = to_cell
        self.board[tr][tc] = self.board[fr][fc]
        self.board[fr][fc] = 0

    def remove_lines(self):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        to_remove = set()
        scores = 0

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]:
                    for dr, dc in directions:
                        line = []
                        r, c = row, col
                        while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == self.board[row][col]:
                            line.append((r, c))
                            r += dr
                            c += dc
                        if len(line) >= LINE_LENGTH:
                            to_remove.update(line)
                            scores += SCORES.get(len(line), 0)

        for r, c in to_remove:
            self.board[r][c] = 0

        self.score += scores
        return bool(to_remove)

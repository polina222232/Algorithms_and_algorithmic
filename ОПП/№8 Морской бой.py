class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == "miss":
            self.map[row][col] = "*"
        elif result == "hit":
            self.map[row][col] = "x"
        elif result == "sink":
            self.map[row][col] = "x"
            # Помечаем клетки вокруг потопленного корабля
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and self.map[nr][nc] == ".":
                    self.map[nr][nc] = "*"

    def cell(self, row, col):
        return self.map[row][col]

# Примеры использования
sm = SeaMap()
sm.shoot(2, 0, 'miss')
sm.shoot(6, 9, 'miss')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()

sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()

sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()

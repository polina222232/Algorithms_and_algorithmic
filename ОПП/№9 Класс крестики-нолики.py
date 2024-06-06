class TicTacToeBoard:
    def __init__(self):
        self.new_game()

    def new_game(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

    def get_field(self):
        return self.field

    def check_field(self):
        
        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] != '-':
                return self.field[i][0]
            if self.field[0][i] == self.field[1][i] == self.field[2][i] != '-':
                return self.field[0][i]
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != '-':
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] != '-':
            return self.field[0][2]
        # Проверка на ничью
        if all(cell != '-' for row in self.field for cell in row):
            return 'D'
        # Продолжаем игру
        return None

    def make_move(self, row, col):
        if not (1 <= row <= 3 and 1 <= col <= 3):
            return "Клетка с координатами ({}, {}) вне поля.".format(row, col)
        if self.field[row - 1][col - 1] != '-':
            return "Клетка ({}, {}) уже занята.".format(row, col)
        if self.game_over:
            return "Игра уже завершена."
        
        self.field[row - 1][col - 1] = self.current_player
        winner = self.check_field()
        if winner:
            self.game_over = True
            return "Победил игрок {}".format(winner)
        
        self.current_player = 'X' if self.current_player == '0' else '0'
        return "Продолжаем играть"

board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")

print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
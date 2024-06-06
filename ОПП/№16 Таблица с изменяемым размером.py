class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.table[row][col]
        return None

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        if 0 <= row < self.rows:
            del self.table[row]
            self.rows -= 1

    def delete_col(self, col):
        if 0 <= col < self.cols:
            for row in self.table:
                del row[col]
            self.cols -= 1

    def add_row(self, row):
        if 0 <= row <= self.rows:
            self.table.insert(row, [0] * self.cols)
            self.rows += 1

    def add_col(self, col):
        if 0 <= col <= self.cols:
            for row in self.table:
                row.insert(col, 0)
            self.cols += 1


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
tab.add_row(1)
tab.add_col(1)
for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
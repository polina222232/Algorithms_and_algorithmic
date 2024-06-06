class BoundingRectangle:
    def __init__(self):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')

    def add_point(self, x, y):
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def width(self):
        return self.max_x - self.min_x

    def height(self):
        return self.max_y - self.min_y

    def bottom_y(self):
        return self.min_y

    def top_y(self):
        return self.max_y

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x

# Примеры использования
rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())  # Выводит -1 3
print(rect.bottom_y(), rect.top_y())  # Выводит -2 4
print(rect.width(), rect.height())    # Выводит 4 6

rect = BoundingRectangle()
rect.add_point(10, 20)
rect.add_point(5, 7)
rect.add_point(6, 3)
print(rect.left_x(), rect.right_x())  # Выводит 5 10
print(rect.bottom_y(), rect.top_y())  # Выводит 3 20
print(rect.width(), rect.height())    # Выводит 5 17

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())  # Выводит -15 13
print(rect.bottom_y(), rect.top_y())  # Выводит -14 10
print(rect.width(), rect.height())    # Выводит 28 24

rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())    # Выводит 34 50
print(rect.left_x(), rect.right_x())  # Выводит -21 13
print(rect.bottom_y(), rect.top_y())  # Выводит -14 36

rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())  # Выводит -14 78
print(rect.width(), rect.height())    # Выводит 68 92
print(rect.left_x(), rect.right_x())  # Выводит -55 13

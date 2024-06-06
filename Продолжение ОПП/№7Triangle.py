class Triangle:
    def __init__(self, side_A, side_B, side_C):
        self.side_A = side_A
        self.side_B = side_B
        self.side_C = side_C

    def perimeter(self):
        return self.side_A + self.side_B + self.side_C


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


# Пример использования
triangle = Triangle(3, 4, 5)
print("Периметр треугольника:", triangle.perimeter())

equilateral_triangle = EquilateralTriangle(3)
print("Периметр равностороннего треугольника:", equilateral_triangle.perimeter())

import math
from PIL import Image, ImageDraw

class RegularPolygon:
    def __init__(self, num_sides, center, radius):
        self.num_sides = num_sides
        self.center = center
        self.radius = radius

    def draw(self, image, color="black"):
        draw = ImageDraw.Draw(image)
        angle = 2 * math.pi / self.num_sides
        points = [
            (self.center[0] + self.radius * math.cos(i * angle),
             self.center[1] + self.radius * math.sin(i * angle))
            for i in range(self.num_sides)
        ]
        draw.polygon(points, outline=color)

# Пример использования:
image = Image.new("RGB", (400, 400), "white")
polygon = RegularPolygon(20, (200, 200), 100)
polygon.draw(image, "red")
image.show()  # или image.save("polygon.png")

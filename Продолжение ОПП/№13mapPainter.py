import PIL
from PIL import ImageColor


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.colors = {}

    def numbers(self):
        return sorted(set(num for row in self.draw_map for num in row))

    def set_color(self, number, color):
        self.colors[number] = color

    def set_cell_size(self, cell_size):
        self.cell_size = cell_size

    def size(self):
        width = len(self.draw_map[0]) * self.cell_size
        height = len(self.draw_map) * self.cell_size
        return width, height

    def draw(self):
        width, height = self.size()
        image = PIL.Image.new("RGB", (width, height), "white")
        pixels = image.load()

        for y, row in enumerate(self.draw_map):
            for x, number in enumerate(row):
                color = self.colors.get(number, "black")
                for i in range(self.cell_size):
                    for j in range(self.cell_size):
                        pixels[x*self.cell_size + i, y*self.cell_size + j] = color if isinstance(color, tuple) else ImageColor.getrgb(color)
        return image

# Пример использования:
drawer = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 20)
colors = {1: 'black', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'lightblue', 7: 'blue', 8: 'violet', 9: 'white'}
for number, color in colors.items():
    drawer.set_color(number, color)

image = drawer.draw()
image.show()  # или image.save("output.png")

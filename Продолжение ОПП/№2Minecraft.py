class BaseObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return [self.x, self.y, self.z]


class Block(BaseObject):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None


class Entity(BaseObject):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass


block = Block(1, 2, 3)
print("Block coordinates before shatter:", block.get_coordinates())
block.shatter()
print("Block coordinates after shatter:", block.get_coordinates())

# Создание объекта Entity
entity = Entity(4, 5, 6)
print("Entity coordinates before move:", entity.get_coordinates())
entity.move(7, 8, 9)
print("Entity coordinates after move:", entity.get_coordinates())

# Создание объекта Thing
thing = Thing(10, 11, 12)
print("Thing coordinates:", thing.get_coordinates())

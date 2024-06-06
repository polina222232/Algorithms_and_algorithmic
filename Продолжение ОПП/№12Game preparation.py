class Weapon:
    def __init__(self, name, damage, range_):
        self.name = name
        self.damage = damage
        self.range = range_

    def hit(self, actor, target):
        if not target.is_alive():
            print("Враг уже повержен")
        else:
            distance = ((actor.pos_x - target.pos_x) ** 2 + (actor.pos_y - target.pos_y) ** 2) ** 0.5
            if distance > self.range:
                print(f"Враг слишком далеко для оружия {self.name}")
            else:
                print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
                target.get_damage(self.damage)

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.inventory = []
        self.current_weapon_index = None

    def hit(self, target):
        if self.current_weapon_index is None:
            print("Я безоружен")
        elif isinstance(target, BaseEnemy):
            self.inventory[self.current_weapon_index].hit(self, target)
        else:
            print("Могу ударить только Врага")

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.inventory.append(weapon)
            print(f"Подобрал {weapon}")
            if self.current_weapon_index is None:
                self.current_weapon_index = 0
        else:
            print("Это не оружие")

    def next_weapon(self):
        if self.current_weapon_index is None:
            print("Я безоружен")
        elif len(self.inventory) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon_index = (self.current_weapon_index + 1) % len(self.inventory)
            print(f"Сменил оружие на {self.inventory[self.current_weapon_index]}")

    def heal(self, amount):
        self.hp = min(200, self.hp + amount)
        print(f"Полечился, теперь здоровья {self.hp}")

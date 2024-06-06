class User:
    def __init__(self, name):
        self.name = name
        self.wall = []

    def send_message(self, user, message):
        print(f"{self.name} отправил сообщение {user.name}: {message}")

    def post(self, message):
        self.wall.append(message)
        print(f"{self.name} выложил пост: {message}")

    def info(self):
        return ""

    def describe(self):
        print(f"Имя: {self.name}\n{self.info()}")


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date
        self.subscriptions = []

    def info(self):
        return f"Дата рождения: {self.birth_date}"

    def subscribe(self, user):
        self.subscriptions.append(user)

        print(f"{self.name} подписался на {user.name}")


class Community(User):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"


# Примеры использования
person = Person("Alice", "01-01-1990")
community = Community("Python Community", "A community for Python enthusiasts")

person.describe()
community.describe()

person.post("Hello, world!")
community.post("Welcome to the Python Community!")

person.send_message(community, "Can I join?")
person.subscribe(community)

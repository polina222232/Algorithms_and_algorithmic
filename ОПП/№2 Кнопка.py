class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def click_count(self):
        return self.clicks

    def reset(self):
        self.clicks = 0

button = Button()

button.click()
button.click()
#button.click()
print(button.click_count())  # Выводит 3

#button.reset()
button.click()
print(button.click_count())  # Выводит 0

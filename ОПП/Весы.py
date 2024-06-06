class Balance:
    def __init__(self):
        self.left_weight = 0
        self.right_weight = 0

    def add_right(self, weight):
        self.right_weight += weight

    def add_left(self, weight):
        self.left_weight += weight

    def result(self):
        if self.left_weight == self.right_weight:
            return "="
        elif self.left_weight > self.right_weight:
            return "L"
        else:
            return "R"
balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())
#balance = Balance()
#balance.add_right(10)
#balance.add_left(5)
#balance.add_left(5)
#print(balance.result())
#balance.add_left(1)
#print(balance.result())

class SparseArray:
    def __init__(self):
        self.data = {}

    def __setitem__(self, index, value):
        if value == 0:
            self.data.pop(index, None)
        else:
            self.data[index] = value

    def __getitem__(self, index):
        return self.data.get(index, 0)

# Примеры использования
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print(f'arr[{i}] = {arr[i]}')  # arr[1] = 10, arr[8] = 20, остальные arr[i] = 0
arr[10] = 123
for i in range(8, 13):
    print(f'arr[{i}] = {arr[i]}')

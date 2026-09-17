import ctypes


class DynamicArray:
    def __init__(self) -> None:
        self.count = 0
        self.capacity = 1
        self.storage = (self.capacity * ctypes.py_object)()

    def __len__(self):
        return self.count

    def __getitem__(self, index):
        if 0 <= index <= (self.count - 1):
            return self.storage[index]
        else:
            raise IndexError

    def append(self, item):

        if self.count == 0:
            self.storage[self.capacity - 1] = item
            self.count += 1

        elif self.count == self.capacity:
            self._resize(self.capacity + 1)
            self.storage[self.capacity - 1] = item
            self.count += 1

        else:
            self.storage[self.capacity - 1] = item
            self.count += 1

    def _resize(self, new_capacity):
        self.temp_storage = (new_capacity * ctypes.py_object)()
        for _ in range(self.capacity):
            self.temp_storage[_] = self.storage[_]
        self.capacity = new_capacity
        self.storage = self.temp_storage


# test suite

dynamic_array = DynamicArray()

dynamic_array.append("aziz")
dynamic_array.append("aziz")

print(dynamic_array[1])
print(len(dynamic_array))

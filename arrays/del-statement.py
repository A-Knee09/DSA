import ctypes


class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0

        self.array = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self, element):
        if self.size == self.n:
            return self.__resize(self.size * 2)

        self.array[self.n] = element
        self.n += 1

    def __resize(self, new_size):
        new_array = self.__make_array(new_size)
        self.size = new_size

        for item in range(self.n):
            new_array[item] = self.array[item]

        self.array = new_array

    def __str__(self):
        result = ""
        for item in range(self.n):
            result += f"{str(self.array[item])}, "

        return f"[{result.rstrip(", ")}]"

    def __getitem__(self, index):
        if index < 0:
            index += self.n

        if 0 <= index <= self.n:
            return self.array[index]
        else:
            return f"IndexError: Index out of range"

    def pop(self):
        if self.n == 0:
            return f"Array is empty cannot pop"

        popped_value = self.array[self.n]
        self.n -= 1
        return popped_value

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.array[i] == item:
                print(f"{item} found at index {i}")
                return
        print(f"ValueError: {item} not found in list")

    def insert_at_pos(self, position, item):
        if self.size == self.n:
            self.__resize(self.size * 2)

        for i in range(self.n, position, -1):
            self.array[i] = self.array[i - 1]

        self.array[position] = item
        self.n += 1

    def __delitem__(self, position):
        if position < 0:
            position += self.n
        if 0 <= position <= self.n:
            for i in range(position, self.n - 2):
                self.array[i] = self.array[i + 1]
            self.n -= 1


dl = MyList()
print(dl)
dl.append(10)
dl.append(20)
dl.append(30)

dl.insert_at_pos(1, 20)
print(dl)
del dl[100]
print(dl)

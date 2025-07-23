import ctypes


class MyList:
    """A class representing a dynamic array"""

    def __init__(self):
        self.size = 1
        self.n = 0

        self.array = self.__make_array(self.size)

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __len__(self):
        return self.n

    def append(self, element):
        if self.n == self.size:
            self.__resize(self.size * 2)

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
        """Method to fetch an item using index"""

        # If negative index turn it to positive one
        if index < 0:
            index += self.n
        if 0 <= index <= self.n:
            return self.array[index]
        else:
            return f"IndexError: Index out of range"


dynamic_list = MyList()
print(f"Data type of dynamic list: {type(dynamic_list)}")
print(f"Dyanmic List : {dynamic_list}")

dynamic_list.append(10)
dynamic_list.append("Hello")
dynamic_list.append(6.9)
print(f"Length/Size of the dynamic list: {len(dynamic_list)}")
print(dynamic_list)

print(dynamic_list[-4])

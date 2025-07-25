"""
Making a class that will behave exactly like lists.
I'm using a module called ctypes for this, which will allow me to use C compatible data types
So I'll make my own dynamic array(lists) using ctypes
"""

import ctypes


class MyList:

    def __init__(self):
        """A class representing a dynamic array"""
        self.size = 1
        self.n = 0  # Number of elements

        # Create a c type array with size = self.size
        self.array = self.__make_array(self.size)

    def __make_array(self, capacity):
        # creates a c type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """Dunder method used to define behaviour of the inbuilt len() function for custom objects"""
        return self.n

    def __resize(self, new_size):
        # Create a new array with new capacity
        new_array = self.__make_array(new_size)
        self.size = new_size

        # Copy the content of the old array to the new one
        for item in range(self.n):
            new_array[item] = self.array[item]

        # Reassign new_array as self.array
        self.array = new_array

    def append(self, element):
        if self.size == self.n:
            # Resize the array
            return self.__resize(self.size * 2)

        self.array[self.n] = element
        self.n += 1

    def __str__(self):
        """Print the the array"""
        result = ""
        for item in range(self.n):
            result += f"{str(self.array[item])}, "

        return f"[{result.rstrip(", ")}]"

    def __getitem__(self, index):
        """Method to fetch an item using index"""
        if index < 0:
            index += self.n

        if 0 <= index <= self.n:
            return self.array[index]
        else:
            return f"IndexError: Index out of range"

    def pop(self):
        """Remove the last item of the array"""
        if self.n == 0:
            return f"Array is empty cannot pop"

        popped_value = self.array[self.n]
        self.n -= 1
        return popped_value

    def clear(self):
        """Remove all elements of the array"""
        self.n = 0
        self.size = 1

    def find(self, item):
        """Find a value in list and return its index"""
        for i in range(self.n):
            if self.array[i] == item:
                return i
        return "ValueError: item not found in list"

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
            for i in range(position, self.n - 1):
                self.array[i] = self.array[i + 1]
            self.n -= 1
        else:
            print(f"IndexError: Index {position} is not in range")

    def remove(self, value):
        pos = self.find(value)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos


dl = MyList()
print(dl)
dl.append(10)
dl.append(20)
dl.append(30)

dl.insert_at_pos(1, 20)
print(dl)
dl.remove(20)
print(dl)

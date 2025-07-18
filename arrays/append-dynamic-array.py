import ctypes


class MyList:
    """A class representing a dynamic array"""

    def __init__(self):
        self.size = 1
        self.n = 0  # Number of elements

        # Create a c type array with size = self.size
        self.array = self.__make_array(self.size)

    def __len__(self):
        """Dunder method used to define behaviour of the inbuilt len() function for custom objects"""
        return self.n

    def __make_array(self, capacity):
        # creates a c type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()

    def __resize(self, new_size):
        # Create a new array with new capacity
        new_array = self.__make_array(new_size)
        self.size = new_size

        # Copy the content of the old array to the new one
        for item in range(self.n):
            new_array[item] = self.array[item]

        # Reassign new_array as self.array
        self.array = new_array

    def apppend(self, element):
        if self.n == self.size:
            # Resize the array
            self.__resize(self.size * 2)

        self.array[self.n] = element
        self.n += 1


dynamic_list = MyList()
print(f"Data type of dynamic list: {type(dynamic_list)}")
print(f"Dyanmic List : {dynamic_list}")

dynamic_list.apppend(10)
dynamic_list.apppend("Hello")
dynamic_list.apppend(6.9)
print(f"Length/Size of the dynamic list: {len(dynamic_list)}")

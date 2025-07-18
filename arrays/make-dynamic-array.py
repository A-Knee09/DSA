"""
Making a class that will behave exactly like lists.
I'm using a module called ctypes for this, which will allow me to use C compatible data types
So I'll make my own dynamic array(lists) using ctypes
"""

import ctypes


class MyList:
    """A class representing a dynamic array"""

    def __init__(self):
        self.size = 1
        self.n = 0  # Number of elements

        # Create a c type array with size = self.size
        self.array = self.__make_array(self.size)

    def __make_array(self, capacity):
        # creates a c type array(static, referential) with size capacity
        return (capacity * ctypes.py_object)()


dynamic_list = MyList()
print(f"Data type of dynamic list: {type(dynamic_list)}")
print(f"Dyanmic List : {dynamic_list}")

"""
Assuming I have a bare bones Linked list, and not the previous ones with additional methods
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None
        self.n = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += f"[{str(curr.data)}] -> "
            curr = curr.next
        return f"{result.rstrip('-> ')}"

    def replace_max(self, value):

        if self.head is None:
            return "Empty list"

        max = self.head
        curr = self.head

        while curr is not None:
            if curr.data > max.data:
                max = curr
            curr = curr.next

        max.data = value


ll = LinkedList()
ll.append(1)
ll.append(4)
ll.append(8)
ll.append(0)
print(ll)
ll.replace_max(10)
print(ll)

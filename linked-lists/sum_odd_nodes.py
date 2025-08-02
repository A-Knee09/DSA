"""
Assuming I have a bare bones Linked list, and not the previous ones with additional methods
Also first position is marked as 0 and not 1
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

    def sum_odd_nodes(self):

        temp = self.head
        counter = 0
        sum = 0

        while temp is not None:
            if counter % 2 != 0:
                sum += temp.data

            counter += 1
            temp = temp.next

        print(f"The sum of odd nodes is: {sum}")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(ll)
ll.sum_odd_nodes()

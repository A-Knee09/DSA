class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0  # Count of current nodes in LL

    def __len__(self):
        return self.n

    def insert_at_head(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        self.n += 1

    def __str__(self):

        curr = self.head
        result = ""
        while curr != None:
            result += f"[{str(curr.data)}] -> "
            curr = curr.next
        return f"{result.rstrip('-> ')}"

    def append(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.n += 1

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

        self.n += 1


ll = LinkedList()
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.append(6)
print(f"Lenght of linked list: {len(ll)}")

print(ll)

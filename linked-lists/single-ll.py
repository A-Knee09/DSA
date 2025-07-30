class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0  # Keep count of items in the ll

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
        while curr is not None:
            result += f"[{str(curr.data)}] -> "
            curr = curr.next
        return f"{result.rstrip('-> ')}"

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

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return "Item not found!"

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is None:
            return "Empty linked list"
        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        if self.head is None:
            return "Empty linked list"
        if self.n == 1:
            self.clear()
            return
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def delete_value(self, value):
        if self.head is None:
            return "Linked list is empty"
        if self.head.data == value:
            return self.delete_head()
        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n -= 1
                return
            curr = curr.next
        return "Value not found"

    def search_node(self, value):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return "Value not found"

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                curr.data = value
                return
            curr = curr.next
            pos += 1
        raise IndexError("Index out of range")

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def to_list(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def is_empty(self):
        return self.head is None


ll = LinkedList()

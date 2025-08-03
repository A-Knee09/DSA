class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        """Initial values on object creation"""
        self.head = None
        self.n = 0

    def __len__(self):
        """Returns the number of elements in the linked list"""
        return self.n

    def __str__(self):
        """Print the linked list in []<->[] format"""
        curr = self.head
        result = ""
        while curr is not None:
            result += f"[{curr.data}] <-> "
            curr = curr.next
        return result.rstrip(" <->") if result else "Empty"

    def insert_at_head(self, value):
        """Insert a node at the beginning of the list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.n += 1

    def append(self, value):
        """Insert a node at the end of the linked list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = new_node
            new_node.prev = curr_node

        self.n += 1

    def insert_after(self, after, value):
        """Insert a node after a given node data"""
        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        if curr is None:
            return "Item not found"

        new_node = Node(value)
        new_node.next = curr.next
        if curr.next is not None:
            curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr

        self.n += 1

    def clear(self):
        """Clear the linked list"""
        self.head = None
        self.n = 0

    def delete_head(self):
        """The the head/first node of the linked list"""

        if self.head is None:
            return "Can't delete, list is empty"

        if self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
        self.n -= 1

    def delete_tail(self):
        """Delete the tail/last node of the linked list"""

        if self.head is None:
            return "Can't delete, list is empty"

        if self.head.next is None:
            self.clear()
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.prev.next = None
        self.n -= 1

    def delete_value(self, value):
        """Deletes a given value from the linked list"""
        if self.head is None:
            return "List is empty"

        curr = self.head

        # If head is to be deleted
        if curr.data == value:
            return self.delete_head()

        while curr is not None:
            if curr.data == value:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                self.n -= 1
                return
            curr = curr.next

        return "Value not found"


ll = LinkedList()
print(ll)
print(f"Length of the linked list: {len(ll)}")
ll.insert_at_head(10)
ll.insert_at_head(9)
ll.insert_at_head(4)
ll.append(20)
print(ll)
print(f"Length of the linked list: {len(ll)}")

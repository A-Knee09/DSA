class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.n += 1

    def dequeue(self):
        if self.head is None:
            print("Queue is empty, cannot dequeue.")
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.n -= 1
        print(f"Dequeued: {removed}")

    def getfront(self):
        if self.head is None:
            print("Empty Queue, nothing at front.")
        else:
            print(f"Front element: {self.head.data}")

    def getrear(self):
        if self.tail is None:
            print("Empty Queue, nothing at rear.")
        else:
            print(f"Rear element: {self.tail.data}")

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"[{curr.data}] -> "
            curr = curr.next
        return result.rstrip(" -> ") if result else "Empty Queue"


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue)
queue.dequeue()
print(queue)
queue.getfront()
queue.getrear()

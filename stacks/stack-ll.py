class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class StackLL:

    def __init__(self):
        self.head = None
        self.n = 0

    def push(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.n += 1

    def pop(self):

        if self.head is None:
            print(f"Empty Stack, cannot pop further\n")

        else:
            popped_value = self.head.data
            self.head = self.head.next
            self.n -= 1
            print(f"Popped value: {popped_value}\n")

    def stack_length(self):

        print(f"Length of the stack: {self.n}\n")

    def peek(self):

        if self.head is None:
            print(f"Stack is empty")

        else:
            print(f"Top element: {self.head.data}")

    def __str__(self):

        curr = self.head
        result = ""
        while curr is not None:

            result += f"[{str(curr.data)}] ->"
            curr = curr.next

        return f"{result.rstrip('-> ')}"


stack = StackLL()
while True:
    ops = ["push", "pop", "peek", "length", "print", "quit"]
    for index, op in enumerate(ops):
        print(f"{index+1}. {op}")

    action = input("Enter an action to perform on the stack (option number): ")

    match action:
        case "1":
            element = input("Enter the value: ")
            stack.push(element)

        case "2":
            stack.pop()

        case "3":
            stack.peek()

        case "4":
            stack.stack_length()

        case "5":
            print(stack)

        case "6":
            break

        case _:
            print("ATMKBFJG")

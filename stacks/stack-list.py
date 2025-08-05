"""
[3,2,4,5,345,6]
"""

sep = "-" * 30
arr = []

# while True:
#     prompt = input("Enter an element: ")
#     arr.append(prompt)
#     prompt = input("Enter another (y,n)")
#     if prompt.lower() == "n":
#         break
# print(arr)


def push():
    while True:
        prompt = input("Enter element: ")
        arr.append(prompt)
        reprompt = input("Enter another: y/n: ").lower()

        if reprompt == "n":
            break
    print(sep)


def pop():

    if arr:
        arr.pop()

    else:
        return "Khali hai"

    print(sep)


def peek():

    if arr:
        print(f"Top element: {arr[-1]}")

    else:
        print("Nothing to peek")

    print(sep)


def length():
    print(f"Stack length: {len(arr)}")

    print(sep)


def stack_print():
    print(f"Stack: {arr[::-1]}")

    print(sep)


while True:
    ops = ["push", "pop", "peek", "length", "print", "quit"]
    for index, op in enumerate(ops):
        print(f"{index+1}. {op}")

    action = input("Enter an action to perform on the stack (option number):\n").lower()

    match action:
        case "1":
            push()

        case "2":
            pop()

        case "3":
            peek()

        case "4":
            length()

        case "5":
            stack_print()

        case "6":
            break

        case _:
            print("ATMKBFJG")

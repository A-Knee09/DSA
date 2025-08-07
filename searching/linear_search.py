def linear_search(arr, target: int):

    for index, element in enumerate(arr):
        if element == target:
            print(f"Target element '{target}' found at index [{index}]")
            break
    else:
        print(f"Target element '{target}' not found in the array")


def prompt():
    arr = []

    while True:
        try:
            item_input = int(input("Enter an integer: "))
            arr.append(item_input)

        except ValueError:
            print(f"Only integer values please")
            continue

        another = input("Would you like to add another item (y/n): ")

        if another.lower() == "n":
            break

    while True:
        try:
            target = int(input("Enter the target: "))
            break

        except ValueError:
            print("Invalid Target, must be an integer")

    linear_search(arr, target)


prompt()

from dataclasses import dataclass
from typing import List


@dataclass
class Stack:
    items: List[object]

    def __init__(self):
        self.items = []

    def push(self, item: object):
        self.items.append(item)

    def pop(self) -> object:
        return self.items.pop()

    def peek(self) -> object:
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []

    def __str__(self) -> str:
        return self.items.__str__()


#  Brief example
def app():
    stack = Stack()

    # Check to make sure starting empty
    print("Stack is empty? {}".format(stack.is_empty()))

    # Fill the stack
    stack.push("This")
    stack.push("is")
    stack.push("a")
    stack.push("stack!")

    # Check to make sure its not empty
    print("Is the stack empty now? {}".format(stack.is_empty()))
    print("What is the stack size? {}".format(stack.size()))
    print("Here is your stack: {}".format(stack))

    print("Popping items off top:")
    for i in range(0, stack.size()):
        print(stack.pop())

    print("Here is what's left: {}".format(stack))
    print("Is the stack empty? {}".format(stack.is_empty()))


if __name__ == "__main__":
    app()

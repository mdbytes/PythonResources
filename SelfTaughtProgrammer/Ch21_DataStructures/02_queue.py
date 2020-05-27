from dataclasses import dataclass
from typing import List


@dataclass
class Queue:
    items: List[object]

    def __init__(self):
        self.items = []

    def enqueue(self, item: object):
        self.items.insert(0, item)

    def dequeue(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return self.items == []

    def __str__(self) -> str:
        return self.items.__str__()


# A brief example
def app():
    queue = Queue()

    print("size of queue: {}".format(queue.size()))
    for i in range(1, 6):
        print("putting '{}' in queue".format(i))
        queue.enqueue(i)

    print("size of queue: {}".format(queue.size()))
    for j in range(1, 6):
        print("removing '{}' from queue".format(queue.dequeue()))

    print("size of queue: {}".format(queue.size()))


if __name__ == '__main__':
    app()

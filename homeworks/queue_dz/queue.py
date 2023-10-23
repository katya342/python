from collections import deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def add_elem(self, item):
     self.items.append(item)

    def peek(self):
       return self.items[0]
    
    def __str__(self):
       return str(self.items)

if __name__ == "__main__":
    queue_1 = Queue()
    queue_1.add_elem(2)
    queue_1.add_elem(3)
    queue_1.add_elem(4)
    print(queue_1.peek())
    print(queue_1)
    
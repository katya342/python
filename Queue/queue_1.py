from collections import deque

class Queue:
    def __init__(self):
        self.length = 0
        self.items = deque()

    def is_empty(self):
        if self.length <= 0 or self.length == None:
            self.length = 0
        return self.length == 0
    
    def insert(self, cargo):
        self.length += 1
        self.items.append(cargo)

    def remove(self):
        self.length -= 1
        if self.length <= 0:
            return None
        self.items.pop()

    def insert_top(self, cargo):
        self.length += 1
        self.items.appendleft(cargo)

if __name__ == "__main__":
   queue = Queue()
   queue.insert_top(2)
   queue.insert_top(3)
   queue.insert_top(4)

   print(queue.is_empty())
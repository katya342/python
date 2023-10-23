class StringStack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    string_stack = StringStack(max_size=2)  

    string_stack.push("hello")
    string_stack.push("world")
    string_stack.push("third_item")  

    print("Stack size:", string_stack.size())
    print("Top item:", string_stack.peek())

    while not string_stack.is_empty():
        item = string_stack.pop()
        print("Popped item:", item)

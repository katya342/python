class StringStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

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
    string_stack = StringStack()

    string_stack.push("hello")
    string_stack.push("world")

    print("Stack size:", string_stack.size())
    print("Top item:", string_stack.peek())

    while not string_stack.is_empty():
        item = string_stack.pop()
        print("Popped item:", item)

from collections import deque

class ShopQueue:
    def __init__(self):
        self.length = 0
        self.items = deque()

    def add_customers(self, customers):
        self.length += 1
        self.items.append(customers)

    def show_queue(self):
        return self.items

if __name__ == "__main__":
    shop = ShopQueue()
    shop.add_customers("Katya")
    shop.add_customers("Katidza")

    print(shop.show_queue())
    







  



class Money:
    def __init__(self, cash, pennies):
        self.cash = cash
        self.pennies = pennies
    def set_cash(self, cash):
        self.cash = cash
    def set_pennies(self, pennies):
        self.pennies = pennies
    def print(self):
        print(f"Dollars: {self.cash} pennies: {self.pennies}")
if __name__ == "__main__":
    moneys = Money("23$", "5")
    moneys.print()
    moneys.set_pennies(23)
    moneys.set_cash(2)
    moneys.print()

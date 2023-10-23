class Figure:
    def __init__(self, a):
        self.a = a
    def calculate(self) -> None:
        pass


class Rectangle(Figure):
    def __init__(self, a):
        self.a = a
    def calculate(self):
        return self.a * self.a

class RightTriangle(Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    def calculate(self):
        return self.a * self.b
class Trapezoid(Figure):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c
    def calculate(self):
        return (self.a + self.b) * self.c / 2
if __name__ == "__main__":
    figure = Rectangle(2)
    temp = figure.calculate()
    print(temp)
    figure_2 = RightTriangle(3, 4)
    temp_2 = figure_2.calculate()
    print(temp_2)
    figure_3 = Trapezoid(3, 4, 5)
    temp = figure_3.calculate()
    print(temp)
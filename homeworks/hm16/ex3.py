import pickle
class Shape:
    def __init__(self, name):
            self.name = name
    def show(self):
        print(f"Figure info:  {self.name}")
    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

class Square(Shape):
    def __init__(self, x1, y1, a, name):
        self.x1 = x1
        self.y1 = y1
        self.a = a
        self.name = name

class Circle(Shape):
    def __init__(self, x1, y1, r, name):
        self.x1 = x1
        self.y1 = y1
        self.r = r
        self.name = name

class Ellipse(Shape):
    def __init__(self, x, y, width, height, name):
        self.x = x
        self. y = y
        self.width = width
        self.height = height
        self.name = name
if __name__ == "__main__":
   figure_1 = Square(2, 4, 10, "Square")
   figure_1.show()
   figure_2 = Circle(3, 3, 5, "Circle")
   figure_2.show()
   figure_3 = Ellipse(2, 3, 5, 6, "Ellipse")
   figure_3.show()
   figure_1.save("example.txt")
   figures = [
       figure_1, 
       figure_2
   ]
   
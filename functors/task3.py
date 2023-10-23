class PositiveNumber:
    def __init__(self, number):
        self.number = number

    def __get__():


class MyClass:
    attribute = PositiveNumber(10)

    def __init__(self, value):
        self._value = value



if __name__ == "__main__":
   obj = MyClass(42)
   obj.attribute
   obj._value = 25
class CustomAttribute:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_vvalue = max_value
        self._value = None


    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_vvalue):
            raise ValueError(f"Value must be in range of {self.min_value} to {self.max_vvalue}")
        self._value = value

class MyClass:
    attribute = CustomAttribute(10, 20)

    def __init__(self, value):
        self._value = value



if __name__ == "__main__":
   obj = MyClass(42)
   obj.attribute
   obj._value = 25
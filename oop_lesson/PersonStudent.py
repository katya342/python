class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"Name: {self.name} Age: {self.age}"

class Courses():
    def __init__(self, courses = []):
        self.courses = courses
 

class Student(Person, Courses):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
      
    def info(self):
        return f"Name: {self.name} Age: {self.age} Id: {self.id}, Courses: {self.courses}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def info(self):
        return f"Name: {self.name} Age: {self.age} Subject: {self.subject}"

if __name__ == "__main__":
   person = Person("Alice", 30)
   student = Student("Bob", 25, "12345")
   teacher = Teacher("Charlie", 35, "Math")
   courses = Courses("Physics")

   print(person.info())
   print(student.info())
   print(teacher.info())
   

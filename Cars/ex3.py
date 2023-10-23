class Employer:
    def print(self):
        print("This is employee class")
    

class President(Employer):
    def __str__(self) -> str:
        return f"President Employer"

class Manager(Employer):
    def __str__(self) -> str:
        return super().__str__()

if __name__ == "__main__":
    emp = President()
    emp.print()
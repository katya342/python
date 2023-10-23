class Passport:
    def __init__(self, name, surname, date):
        self.name = name
        self.surname = surname
        self.date = date
    def info(self):
        print(f"{self.name} {self.date} {self.surname}")

class ForeignPassport(Passport):
    def __init__(self, name, surname, date, number):
        super().__init__(name, surname, date)
        self.number = number
        self.visas = []
    def info(self):
        print(f"{self.name} {self.date} {self.surname} {self.number}")
    
    def add_visa(self, visa):
        return self.visas.append(visa)

    def visas_info(self):
        for visa in self.visas:
            print(visa.country, visa.number)

class Visa:
    def __init__(self,country, number):
        
        self.country = country
        self.number = number
    def info(self):
        print(f"{self.country} {self.number}")


if "__main__" in __name__:
    foreign_pass = ForeignPassport("Katya", "Bezverkhova", "25.12.2002", "123455")
    foreign_pass.info()
    visa1 = Visa('Germany', "001-1111")
    foreign_pass.add_visa(visa1)
    foreign_pass.visas_info()



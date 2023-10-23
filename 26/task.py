class Rail:
    def __init__(self, number):
        self.number = number
        
class Vehicle:
    def __init__(self, type: object):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def __repr__(self) -> str:
        return f'Type: {self.type}'
        
    def __str__(self) -> str:
        return f"Vehicle type: {self.type}"
    
class Bus(Vehicle):
    def __init__(self, number: str):
        self.number = number
    
    def get_number(self) -> str:
        return self.number
    
    def __repr__(self) -> str:
        return f"Number is {self.number} vehicle type is {self.type}"
    
    def __str__(self) -> str:
        return f"Vehicle type is {self.type} number is {self.number}"
    
class BusSchedule(Vehicle):
    def __init__(self, list):
        self.list = []
    
    def add_bus(self, bus_number:str, departure_time: str) -> list:
        self.list.append((bus_number, departure_time))
  
    
    def is_bus(self, vehicle_number: str) -> bool:
        for item in self.list:
            if item[0].number == vehicle_number:
                return True
            else:
                return False
    def check_schedule(self, bus_number: str, departure_time: str) -> bool:
        if (bus_number, departure_time) in self.list:
            return True
        else:
            return False

    def get_schedule(self) -> list:
        return self.list
    
    def get_schedule_by_bus_number(self, bus_number: str) -> list:
        temp = self.get_schedule()
        for item in temp:
            if item[0].number == bus_number:
                return temp



if __name__ == "__main__":
    obj1 = Vehicle("Bus")
    bus1 = Bus("100")
    schedule = BusSchedule()
    schedule.add_bus(bus1, "09:00")
    print(repr(obj1))
    print(obj1)
    schedule.is_bus()
    schedule.check_schedule()

import datetime

class DateTimeManager:
    def __init__(self, date: int):
        self.date = datetime.datetime.now()  
    
    def add_days(self, days: int) -> None:
        self.date += datetime.timedelta(days=days) 

    def subtract_days(self, days: int) -> None:
        self.date -= datetime.timedelta(days=days)

    def format_date(self, format_string: str) -> str:
        return self.date.strftime(format_string)

if __name__ == "__main__":
    obj = DateTimeManager(2)
    obj.add_days(34) 
    print(obj.date)
    formatted_date = obj.format_date("%Y-%m-%d %H:%M:%S")   
    print("Formatted Date:", formatted_date)

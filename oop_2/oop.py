class Wheels:
       # Класс, представляющий колеса автомобиля
    def __init__(self, num_wheels: int):
        # Инициализация колес
        self.num_wheels = num_wheels
    
    def rotate(self):
        # Вращает колеса
        print(f"{self.num_wheels} колеса вращаются")

class Engine:
    # Класс, представляющий двигатель автомобиля.

    def start(self): 
        # Запускает двигатель
        print("Двигатель запущен")

    def stop(self):
        # Останавливает двигатель
        print("Двигатель остановлен")

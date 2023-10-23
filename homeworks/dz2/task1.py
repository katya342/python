def calculate_1():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    print("Выберите операцию:")
    print("1. Сумма трех чисел")
    print("2. Произведение трех чисел")
    choice = input("Введите номер операции (1/2): ")
    if choice == "1":
        result = num1 + num2 + num3
        print(f"Сумма трех чисел: {result}")
    elif choice == "2":
        result = num1 * num2 * num3
        print(f"Произведение трех чисел: {result}")
    else:
        print("Некорректный ввод операции. Пожалуйста, выберите 1 или 2.")

def calculate_2():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    print("Выберите операцию:")
    print("1. Найти максимум из трех чисел")
    print("2. Найти минимум из трех чисел")
    print("3. Найти среднеарифметическое трех чисел")
    choice = input("Введите номер операции (1/2/3): ")
    if choice == "1":
        result = max(num1, num2, num3)
        print(f"Максимум из трех чисел: {result}")
    elif choice == "2":
        result = min(num1, num2, num3)
        print(f"Минимум из трех чисел: {result}")
    elif choice == "3":
        result = (num1 + num2 + num3) / 3
        print(f"Среднеарифметическое трех чисел: {result}")
    else:
        print("Некорректный ввод операции. Пожалуйста, выберите 1, 2 или 3.")
def calculate_3():
    # Получаем ввод от пользователя для количества метров
    meters = float(input("Введите количество метров: "))

# Предоставляем пользователю выбор единицы измерения
    print("Выберите единицу измерения:")
    print("1. Мили")
    print("2. Дюймы")
    print("3. Ярды")

    choice = input("Введите номер единицы измерения (1/2/3): ")

    if choice == "1":
    # Выбрана единица измерения "Мили"
        miles = meters / 1609.34  # 1 метр = 0.000621371 мили (приближенно)
        print(f"{meters} метров равно приблизительно {miles} милям")
    elif choice == "2":
    # Выбрана единица измерения "Дюймы"
        inches = meters * 39.3701  # 1 метр = 39.3701 дюйма
        print(f"{meters} метров равно приблизительно {inches} дюймам")
    elif choice == "3":
    # Выбрана единица измерения "Ярды"
        yards = meters * 1.09361  # 1 метр = 1.09361 ярда
        print(f"{meters} метров равно приблизительно {yards} ярдам")
    else:
        print("Некорректный ввод единицы измерения. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    # calculate_1()
    # calculate_2(
    # )
    # calculate_3()
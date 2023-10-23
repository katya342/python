def main():
    meters = float(input("Введите количество метров: "))
    print("Выберите единицу измерения для перевода:")
    print("1 - Мили")
    print("2 - Дюймы")
    print("3 - Ярды")
    choice = int(input("Введите номер выбора: "))
    if choice == 1:
        miles = meters * 0.000621371
        print(f"{meters} метров равно {miles} милям.")
    elif choice == 2:
        inches = meters * 39.3701
        print(f"{meters} метров равно {inches} дюймам.")
    elif choice == 3:
        yards = meters * 1.09361
        print(f"{meters} метров равно {yards} ярдам.")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()

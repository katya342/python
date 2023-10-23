# Инициализация базы данных сотрудников как словаря
employees = {}

# Функция для добавления нового сотрудника
def add_employee():
    name = input("Введите имя сотрудника: ")
    surname = input("Введите фамилию сотрудника: ")
    age = int(input("Введите возраст сотрудника: "))
    employees[surname] = {'Имя': name, 'Фамилия': surname, 'Возраст': age}
    print(f"Сотрудник {name} {surname} добавлен в базу данных.")

# Функция для редактирования данных сотрудника
def edit_employee():
    surname = input("Введите фамилию сотрудника, данные которого вы хотите отредактировать: ")
    if surname in employees:
        name = input("Введите новое имя сотрудника: ")
        age = int(input("Введите новый возраст сотрудника: "))
        employees[surname]['Имя'] = name
        employees[surname]['Возраст'] = age
        print(f"Данные сотрудника {name} {surname} отредактированы.")
    else:
        print("Сотрудник с такой фамилией не найден.")

# Функция для удаления сотрудника
def delete_employee():
    surname = input("Введите фамилию сотрудника, которого вы хотите удалить: ")
    if surname in employees:
        del employees[surname]
        print(f"Сотрудник {surname} удален из базы данных.")
    else:
        print("Сотрудник с такой фамилией не найден.")

# Функция для поиска сотрудника по фамилии
def search_employee_by_surname():
    surname = input("Введите фамилию сотрудника, которого вы хотите найти: ")
    if surname in employees:
        employee = employees[surname]
        print(f"Имя: {employee['Имя']}")
        print(f"Фамилия: {employee['Фамилия']}")
        print(f"Возраст: {employee['Возраст']}")
    else:
        print("Сотрудник с такой фамилией не найден.")

# Функция для вывода информации обо всех сотрудниках
def list_all_employees():
    print("Информация о всех сотрудниках:")
    for surname, employee in employees.items():
        print(f"Фамилия: {employee['Фамилия']}, Имя: {employee['Имя']}, Возраст: {employee['Возраст']}")

# Главная функция для управления программой
def main():
    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Редактировать данные сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника по фамилии")
        print("5. Вывод информации обо всех сотрудниках")
        print("6. Выйти из программы")
        choice = input("Выберите действие (1/2/3/4/5/6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            edit_employee()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            search_employee_by_surname()
        elif choice == '5':
            list_all_employees()
        elif choice == '6':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()

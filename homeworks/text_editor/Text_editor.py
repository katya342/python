class Record:
    def init(self):
        self.text = ""

    def save(self, filename):
        try:
            with open(filename, "w") as file:
                file.write(self.text)
            print(f"Текст успешно сохранен в файле '{filename}'")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def load(self, filename):
        try:
            with open(filename, "r") as file:
                self.text = file.read()
            print(f"Текст успешно загружен из файла '{filename}'")
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")

class TextEditor:
    def init(self):
        self.text = ""
        self.undo_stack = []

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()
            print("Отмена последнего действия выполнена.")
        else:
            print("Нет действий для отмены.")

    def edit_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text = new_text
        print("Текст успешно отредактирован.")

    def save_file(self, filename):
        try:
            with open(filename, "w") as file:
                file.write(self.text)
            print(f"Текущий текст сохранен в файле '{filename}'")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    @staticmethod
    def menu() -> str:
        print("Меню")
        print("1. Сохранить файл")
        print("2. Загрузить текст")
        print("3. Отменить последнее действие")
        print("4. Выйти")
        return input("Выберите опцию: ")

if __name__ == "__main__":
    record = Record()
    editor = TextEditor()
    
    while True:
        choice = editor.menu()
        if choice == "1":
            filename = input("Введите имя файла для сохранения: ")
            editor.save_file(filename)
        elif choice == "2":
            filename = input("Введите имя файла для загрузки: ")
            record.load(filename)
            editor.text = record.text
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию из меню.")
from pathlib import Path
import pandas as pd
import os


class ToDoList:
    def __init__(self, filename):
        directory_folder = os.path.dirname(os.path.abspath(__file__))
        filename = directory_folder + "/" + filename
        
        if not os.path.exists(filename):
            Path(filename).touch()
            self.filename = filename
            self.tasks = pd.DataFrame(columns=["Date", "Task"])
            self.save_tasks()

        self.filename = filename
        self.tasks = pd.DataFrame(columns=["Date", "Task"])
        self.load_tasks()

directory_folder = os.path.dirname(os.path.abspath(__file__)) # - Получить текущий путь 
filename = directory_folder + "/" + filename # - Создать путь к файлу

Path(filename).touch() # - Создать файл


self.tasks = pd.DataFrame(columns=["Date", "Task"]) # - Загрузить данные из файла по колонкам
pd.ExcelFile(self.filename).sheet_names # - Получить названия листов, проверить существование файла
pd.read_excel(self.filename, header=0) # - Прочитать данные из файла
self.tasks["Task"].tolist() # - Просмотреть все задачи
self.tasks.to_excel(self.filename, index=False) # - Сохранить данные в файл

self.tasks._append(task, ignore_index=True) # - Добавить задачу


self.tasks[self.tasks["Task"] != task].reset_index(drop=True) # - Удалить задачу
pd.DataFrame(columns=["Task"]) # - Очистить список

self.tasks[self.tasks["Task"].str.contains(keyword, case=False, na=False)] # - Поиск задач



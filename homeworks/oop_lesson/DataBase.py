from typing import Any


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs) -> object:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance


    def __init__(self, user, password, port) -> None:
        if not self.__initialized:
            self.user = user
            self.password = password
            self.port = port
            self.__initialized = True
        self.records = []

    def __del__(self) -> None:
        DataBase.__instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.__instance is not None:
            raise TypeError("This class is a singleton")
    def get_user(self):
        return self.user, self.password, self.port
    
    @property
    def records(self) -> list:
        return self.records
   

    @records.setter
    def records(self, data):
        self.records.append(data)
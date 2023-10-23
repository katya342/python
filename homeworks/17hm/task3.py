class FileManager:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self) -> str:
        try:
            with open(self.file_name, "r") as file:
                file_content = file.read()
                return file_content
        except FileNotFoundError:
            print("File was not found")

    def write_to_file(self, content) -> None:
        with open(self.file_name, "w") as file:
            file.write(content)

if __name__ == "__main__":
    files = FileManager("test.txt")
    print(files.read_file())
    files.write_to_file("KAD")

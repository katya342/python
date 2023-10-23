class ListManipulator:
    def __init__(self, list) -> list:
        self.list = list
    def get_length(self) -> int:
        return len(self.list)
    def add_element(self, element):
        list.append(element)
    def remove_element(self, element: any):
        try:
            self.list.remove(element)
        except ValueError:
            print("Error occured")
            
    def get_element_at_index(self, index: any):
        try:
            return self.list[index]
        except IndexError:
            print("Endex out of range")
    @staticmethod 
    def merge_lists(list1: list, list2: list) -> list:
        return list1 + list2
    

if __name__ == "__main__":
    list_1 = ListManipulator([2, 3, 4, 7, 3])
    print(list_1.get_length())
    list_1.remove_element(3)
    print(list_1.merge_lists([2,3,4,2], [1,8,2]))
    
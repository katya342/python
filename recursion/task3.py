class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.left = None
        self.right = None

    

class PhoneBook:
    def __init__(self):
        self.root = None

    def add_contact(self, name, phone_number):  
        new_contact = Contact(name, phone_number)
        if not self.root:
            self.root = new_contact
        else:
            self._add(self.root, new_contact)
            
            
    def _add(self, node, new_contact):
        if node.name < new_contact.name:
            if node.right is None:
                node.right = new_contact
            else:
                self._add(node.right, new_contact)
        elif node.name > new_contact.name:
            if node.left is None:
                node.left = new_contact
            else:
                self._add(node.left, new_contact)

    def display_contacts(self):
        self._display(self.root)
    
    def _display(self, node):
        if node:
            self._display(node.left)
            print(f"Name: {node.name}, Phone: {node.phone_number}")
            self._display(node.right)
        
    def search_contact(self, name):
        return self._search(self.root, name)
    
    def _search(self, node, name):
        if node is None or node.name == name:
            return node
        
        if node.name < name:
            return self._search(node.right, name)
        
        return self._search(node.left, name)
        

       









if __name__ == "__main__":
  
    phone_book = PhoneBook()


    phone_book.add_contact("John", "123-456-7890")
    phone_book.add_contact("Alice", "987-654-3210")

    result = phone_book.search_contact("Jane Smith")
if result:
    print(f"Contact found - Name: {result.name}, Phone: {result.phone_number}")
else:
    print("Contact not found")

# Выводим все контакты
phone_book.display_contacts()
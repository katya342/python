class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    
    return search(root.left, key)



if __name__ == "__main__":
   root = None

   keys = [15, 2, 3, 20, 15, 10]
   for key in keys:
       root = insert(root, key)

search_key = 10

result = search(root, search_key)
if result:
    print(f"Element {search_key} founded")
else:
    print(f"Element {search_key} no found")


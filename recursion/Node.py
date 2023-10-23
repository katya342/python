class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print("(" + str(node.val) + ")", end = " ")
        inorder_traversal(node.right)


if __name__ == "__main__":
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3)
   root.left.left = Node(4)
   root.left.right = Node(5)

   print("Inorder Traversal:")
   inorder_traversal(root)

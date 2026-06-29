class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def print_structure(self):
        self._print_tree(self.root)

    def _print_tree(self, node):

        if node is None:
            return

        print(node.data)

        self._print_tree(node.left)
        self._print_tree(node.right)
        
root = Node("A")

root.left = Node("B")
root.right = Node("C")

root.left.left = Node("D")
root.left.right = Node("E")

tree = BinaryTree(root)

tree.print_structure()
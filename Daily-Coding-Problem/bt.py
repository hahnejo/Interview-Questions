# create a node
# create a class called binary tree
#   print tree method 
#   preorder print method

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, iter_type):
        if iter_type == "preorder"
            return (self.preorder_print(self.root, ""))

    def preorder_print(self, start, iter):
        if start:

            
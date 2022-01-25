# WIP
class RedBlackTree:
    def __init__(self, *values):
        self.root = None
        for value in values:
            self.insert(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.is_black = True
            return
        node = self.root.insert(value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.is_black = False

    def binary_search(self,value):
        if self.value == value:
            return True
        elif self.left and self.value > value:
            return self.left.binary_search(value)
        elif self.right and self.value < value:
            return self.right.binary_search(value)
        else:
            return False

    def insert(self, value):
        if self.left and self.value > value:
            return self.left.insert(value)
        elif self.value > value:
            self.left = Node(value)
            return self.left
        elif self.right and self.value < value:
            return self.right.insert(value)
        elif self.value < value:
            self.right = Node(value)
            return self.right
        else:
            return None
# WIP
class RedBlackTree:
    def __init__(self, *values):
        self.root = None
        for value in values:
            self.insert(value)

    def print_tree(self):
        i = 0
        frontier = [(self.root, i)]
        flag = True
        while flag:
            flag = False
            buffer = []
            for node, index in frontier:
                if not node:
                    flag = True


    def search(self, value):
        return self.root.binary_search(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.is_black = True
            return
        node = self.root.insert(value)

    def __rotate_left(self, node):
        if not node.right:
            return
        new_head = node.right
        node.right = new_head.left
        new_head.left = node
        if node == self.root:
            self.root = new_head

    def __rotate_right(self, node):
        if not node.left:
            return
        new_head = node.left
        node.left = new_head.right
        new_head.right = node
        if node == self.root:
            self.root = new_head


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


if __name__ == "__main__":  # Only runs if this is the file being run, useful for tests
    print("Hello World")
else:
    print("foobar")
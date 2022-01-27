# WIP

class RedBlackTree:
    def __init__(self, *values):
        self.root = None
        for value in values:
            self.insert(value)

    def print_tree(self):
        frontier = [self.root]
        explored =[]
        flag = True
        while flag:
            flag = False
            buffer = []
            for node in frontier:
                if node:
                    flag = True
                    buffer.append(node.left)
                    buffer.append(node.right)
                else:
                    buffer.append(None)
                    buffer.append(None)
            if flag:
                explored.append(frontier)
            frontier = buffer
        width = len(explored[-1])
        height = len(explored)
        for i in range(height):
            tabs = int(width * (0.5 ** (i + 1))) + 1
            print(("\t" * tabs) + ("\t" * tabs).join(map(str,explored[i])))

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

    def __str__(self):
        return str(self.value)

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
    rbtree = RedBlackTree(5, 2, 7, 1, 3, 6, 8)
    rbtree.print_tree()
    print("Hello World")
else:
    print("foobar")
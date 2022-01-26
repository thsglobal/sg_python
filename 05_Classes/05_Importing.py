# There are two ways to import, first commented out

# import red_black_tree
#
# rbtree = red_black_tree.RedBlackTree(5, 2, 7, 1, 3, 6, 8)

from red_black_tree import RedBlackTree  # Can list multiple imports from a file ie "RedBlackTree, Node"

rbtree = RedBlackTree(5, 2, 7, 1, 3, 6, 8)

print(rbtree.search(2))
print(rbtree.search(4))
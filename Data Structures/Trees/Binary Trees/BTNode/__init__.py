class Node(object):
    """
    Binary Tree node consisting of the tree's root node and it's branches.
           1 - Node value
          / \
         2   3 -- Right Value
         |
        Left value
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


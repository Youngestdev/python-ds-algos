from BSTNode import BSTNode


class BinarySearchTree(object):
    """
    Binary Search Tree. Allocates lesser objects to the left & higher objects to the right.
    """

    def __init__(self, root):
        """
        :param root: Root node
        """
        self.root = BSTNode(root)

    def insert(self, val):
        """
        :param val: New value to be inserted in the search tree.
        :return: Nothing actually.
        """

        self.insert_helper(self.root, val)

    def insert_helper(self, current, new_val):
        """
        :param current: Node to begin insertion ( usually the root )
        :param new_val: The new value to be inserted into the tree
        :return: Nothing actually.
        """

        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = BSTNode(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = BSTNode(new_val)

    def search(self, value):
        """
        :param value: Value to be searched for in the tree
        :return: Return a boolean
        """

        return self.search_helper(self.root, value)

    def search_helper(self, current, value):
        if current:
            if current.value == value:
                return True
            elif current.value < value:
                return self.search_helper(current.right, value)
            else:
                return self.search_helper(current.left, value)

    def balanced(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.value
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, val, upper):
                return True

            return True

        return helper(self.root)

myTree = BinarySearchTree(40)
myTree.insert(25)
myTree.insert(60)
myTree.insert(24)
myTree.insert(80)
print(myTree.balanced())

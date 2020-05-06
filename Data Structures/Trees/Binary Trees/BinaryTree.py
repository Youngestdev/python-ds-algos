from BTNode import Node
from Queue import Queue
from Stacks import Stack


class BinaryTree(object):
    """"
    Binary Tree implementation, it takes a value of type @Node which becomes its root value.
    """

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + " -> "

            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    def MaximumLevelSum(self):
        """
        Uses a similar technique with the Level order traversal
        :return: The tree level with the highest sum.
        """

        start = self.root
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        arr = list()
        arr.append(start.value)

        while len(queue) > 0:
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            if node.left and node.right:
                arr.append(node.left.value + node.right.value)
        return arr.index(max(arr)) + 1


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(0)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree2 = BinaryTree(39608)
tree2.root.left = Node(0)
tree2.root.right = Node(-34332)
tree2.root.left.left = Node(84856)
tree2.root.left.right = Node(62101)
tree2.root.right.left = Node(98129)
tree2.root.right.right = Node(0)
tree2.root.left.left.left = Node(0)
tree2.root.left.left.right = Node(-26118)
tree2.root.right.right.left = Node(0)
tree2.root.right.right.right = Node(57785)
tree2.root.left.left.left.left = Node(-75141)
tree2.root.left.left.left.right = Node(0)
tree2.root.right.right.right.left = Node(0)
tree2.root.right.right.right.right = Node(-63491)
tree2.root.left.left.left.left.left = Node(-63367)

print(tree2.levelorder_print(tree2.root))
# print(tree2.MaximumLevelSum())
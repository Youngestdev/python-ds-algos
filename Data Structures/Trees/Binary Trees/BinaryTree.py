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
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)

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

    def dfsPrint(self, start):
        if start is None:
            return

        stack = Stack()
        stack.push(start)
        traversal = ""
        while len(stack) > 0:
            traversal += str(stack.peek().value) + "->"

            node = stack.pop()
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

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

    def bfsSize(self):

        if self.root is None:
            return 0

        queue = Queue()
        head = self.root
        if head is not None:
            queue.enqueue(head)
        count = 0
        while queue.size() > 0:
            count += 1
            node = queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return count


    def dfsSize(self):
        if self.root is None:
            return 0

        stack = Stack()
        head = self.root
        if head is not None:
            stack.push(head)
        count = 0

        while len(stack) > 0:
            count += 1
            node = stack.pop()
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)

        return count

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


if __name__ == '__main__':
    Tree = BinaryTree(2)
    Tree.root.left = Node(4)
    Tree.root.right = Node(5)
    Tree.root.left.left = Node(6)
    Tree.root.left.right = Node(7)

    print(Tree.size_(Tree.root))
    print(Tree.bfsSize())
    print(Tree.dfsPrint(Tree.root))
    print(Tree.levelorder_print(Tree.root))

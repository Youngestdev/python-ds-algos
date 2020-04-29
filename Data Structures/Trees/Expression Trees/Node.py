class ExpressionTreeNode:
    def __init__(self, data):
        """
        :param data: Arithmetic operator: +, -, /, *
        """
        self.element = data
        self.left = None
        self.right = None
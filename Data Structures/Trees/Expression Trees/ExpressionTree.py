class ExpressionTree:
    """"
        Expression tree class. An expression tree is used for arithmetic computations,
        an example is the tree used in integral-calculator.com
    """

    def __init__(self, exprTree):
        """
        :param exprTree: A parenthesized mathematical expression enclosed in string e.g - "(a / (b-3))"
        """
        self.exprTree = None
        self.buildTree(exprTree)

    def evaluate(self, variablemap):
        """
        :param variablemap: a dictionary containing the arithmetic data. e.g - vars = { 'a' : 5, 'b' : 12 }
        :return: The result from the computation.
        """
        return self.evaluate(self.exprTree, variablemap)

    def __str__(self):
        """
        :return: The string representation of the tree data.
        """
        return self.buildString(self.exprTree)

    def buildTree(self, expTree):
        """
        :param expTree:
        :return: An expression tree
        """
        pass

    def buildString(self, treeNode):
        """
        :param treeNode:
        :return: variables in string format. ( Err.. Idk )
        """
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.element)
        else:
            # Otherwise, it's an operator.
            expstr = '('
            expstr += self._buildString(treeNode.left)
            expstr += str(treeNode.element)
            expstr += self._buildString(treeNode.right)
            expstr += ')'
        return expstr

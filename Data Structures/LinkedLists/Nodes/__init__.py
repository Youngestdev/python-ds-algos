"""
This consists of Node classes - Lists, Graphs ( in the future) etc
"""

class Node(object):
  """
  Node class for Single and Circular list.
  """
  def __init__(self, data):
    self.data = data
    self.next = None

class DoubleNode:
  """
  Node class for Double List.
  """
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

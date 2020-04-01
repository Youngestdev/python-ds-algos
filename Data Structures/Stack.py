class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop()

  def get_stack(self):
    return self.items

  def is_empty(self):
    return len(self.items) == 0


a = Stack()
a.push("abdul")

reversedStr = ""

def revString(Stack, s):
  for i in range(len(s)):
    Stack.push(s[i])
  revstr = ""

  while not Stack.is_empty():
    revstr += Stack.pop()

  return revstr

print(revString(Stack(), "abdul"))
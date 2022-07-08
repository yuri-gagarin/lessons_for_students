class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b; a.right = c; b.left = e; b.right = d; c.right = f;

def traverse_depth_first(node):
  if not node: return []
  stack = [ node ]
  result = []
  while len(stack) > 0:
    current = stack.pop()
    result.append(current)

    print(current.val)

    if current.left: stack.append(current.left)
    if current.right: stack.append(current.right)

  return result

def traverse_depth_first_recursive(node):
  if not node: return []
  print(node.val)

  left_vals = traverse_depth_first_recursive(node.left)
  right_vals = traverse_depth_first_recursive(node.right)
  
  return [ node.val, *left_vals, *right_vals ]



print(traverse_depth_first_recursive(a))
    
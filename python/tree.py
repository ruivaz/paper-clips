class Node:
  def __init__(self, left=None, right=None, value=None):
    self.left=left
    self.right=right
    self.value=value

def add_node(root, value):
  if root.value==None:
    root.value=value
  elif value > root.value:
    if root.right==None:
      root.right=Node(value=value)
    else:
      add_node(root.right, value)
  elif value < root.value:
    if root.left==None:
      root.left=Node(value=value)
    else:
      add_node(root.left, value)


def transverse(root):
  if root==None:
    return
  else:
    transverse(root.left)
    transverse(root.right)
    print root.value
    

root=Node()

add_node(root, 8)
add_node(root, 4)
add_node(root, 6)
add_node(root, 12)
add_node(root, 14)
add_node(root, 13)
add_node(root, 3)

transverse(root)


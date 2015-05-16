#Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.

#build up the BST
class Node(object):
  def __init__(self, data, parent = None, left=None, right=None):
    self.data = data
    self.parent = parent    
    self.left = left
    self.right = right
    
    
  def insert(self, data):
    #check the root data first
    if self.data:
      #check the right hand side
      if(self.data > data):
        if self.left is None:
          self.left = Node(data, self)
        else:
          self.left.insert(data)
      elif(self.data < data):
        if self.right is None:
          self.right = Node(data, self)
        else:
          self.right.insert(data)
    else:
      self.data = data
        
#building the BST
root = Node(42, None)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(40)

#testing
#print root.left.left.parent.parent.right.data

#inorder print left, root, right
def printn(root):
  if root == None:
    return
  printn(root.left)
  print root.data
  printn(root.right)

#1), if the node has a right subtree, largest value in the right subtree is the next value to be selected
#2), if the node does not have a right subtree, let the pointer keep going up through the right path, if the pointer faces a left path, this is the next value to be selected
#3), if the node is the biggest node in the tree, it will not be considered

def nextValue(node):
  #node has a right subtree
  if(node.left != None):
    return find_most_left(node.right)
  #node does have a right subtree
  else:
    while(node.parent != None):
      if node.parent.right == node:
        node = node.parent
      else:
        break;
    if node.parent == None:
      print "third case, the last element"
      return Node("hehe", None)
    return node.parent
    

def find_most_left(node):
  while node.left != None:
    node = node.left
  return node

new = root
print new.data
print nextValue(new).data


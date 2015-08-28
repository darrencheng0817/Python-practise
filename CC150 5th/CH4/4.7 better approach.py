#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

#In this case, we assume BST is BT, I will not use any properties from BST
#build up the BT
class Node(object):
  def __init__(self, data, parent = None, left=None, right=None, color = None):
    self.data = data
    self.parent = parent    
    self.left = left
    self.right = right
    self.color = color
    
    
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
      
  #1),left node1 go first, until hits the root, for each step, node1 sets the color to be "found"
  #2),then node2 start to go up, once it hits "found", return that node  
def common(node1, node2):
  node1.color = "found"
  while node1.parent != None:
    node1.parent.color = "found"
    node1 = node1.parent
  
  #node2 find the common ancestor
  while node2.parent != None:
    if node2.color == "found":
      print node2.data
      return
    node2 = node2.parent
  if node2.color == "found":
      print node2.data
      return 
    
    
    
      
    
    
        
#building the BST
root = Node(42, None)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(40)

common(root.left.left.right, root.right)

#print root.color
#print root.left.color
#print root.left.left.color
#print root.left.left.right.color


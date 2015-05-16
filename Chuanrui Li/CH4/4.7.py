#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

#This is the better solution for BT
#In this case, we assume BST is BT, I will not use any properties from BST
#build up the BT
class Node(object):
  def __init__(self, data, parent = None, left=None, right=None, color = None):
    self.data = data
    self.parent = parent    
    self.left = left
    self.right = right
    #self.color = color
    
    
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

#check the given node is cover by the subtree
def cover(root, node):
  #end of the tree and the 
  if root == None:
    return False
  #find the node in the tree
  if root == node:
    return True
  #This is the recursive step
  return cover(root.right, node) or cover(root.left, node)

#This is for the root value
def common(root, node1, node2):
  #this is the case: one node comes earlier than other node, the first node is an ancestor. root == node
  if node1 == root:
    return node1
  elif node2  == root:
    return node2
  #this is the case, both node1 and node2 are not in the tree
  if root == None:
    print "nodes do not exist"
    return root
  
  sub1 = cover(root.left, node1)
  sub2 = cover(root.left, node2)
  #two nodes seperated on two sides
  if sub1 != sub2:
    return root
  else:
    #both node are on right hand side
    if sub1 == sub2 == False:
      return common(root.right, node1, node2)
    #both node are on left hand side
    elif sub1 == sub2 == True:
      return common(root.left, node1, node2)
      
  

    
    
        
#building the BST
root = Node(42, None)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(40)


print common(root, root, root.left.left.right).data
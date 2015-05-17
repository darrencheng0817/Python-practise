#you are given a binary tree in which each node contains a value. Design an algorithm to print all paths which sum up to that value. Note that it can be any path in the tree - it does not have to start at the root.


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



#Find the depth of Binary Tree for defining the length of array
def depth_tree(root):
  if root == None:
    return 0
  else:
    return 1 + max(depth_tree(root.right), depth_tree(root.left))
  
path = [0]*depth_tree(root)

#bounded by level, do not sum previous stack data
def printlist(value, path, level):
  #print path
  sum_all = 0
  #print "string: " + str(level)
  length = level
  while 0 <= level:
    sum_all += path[level]
    #print sum_all, value
    if sum_all == value:
      #print the value from top to bottom
      i = level
      while i <= length:
        #print i
        print path[i]
        i += 1
      break
    level -= 1
    
    
#Find the paths in the BT and the sum of the path is equal to a constant value
#using the stack, it always First come last out

def sum_find(value, root, path, level):
  if root == None:
    return
  #storing the value from 0(top) to 4(bottom)
  path[level] = root.data
  
  #check the sum of path, from bottom to top
  printlist(value, path, level)
  
  sum_find(value, root.left, path, level+1)
  sum_find(value, root.right, path, level+1)




sum_find(79, root, path, 0)
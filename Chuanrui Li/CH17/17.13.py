#Write a simple node-like data structure called BiNode, which has pointers to two other nodes. The data structure BiNode could be used
#to repesent both a binary tree (where node1 is the left node and node2 is the right node) or a doubly linked list (where node1 is the previous node and node 2 is the next node). Implement a method to convert a binary search tree(implementated with Binode) into a doubly linked list. The value should be kept in order and the operation should be performed in place (that is, on the original data structure)
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
      
  def nextD(self, dataNext):
    self.right = dataNext
      
  def pre(self, parent):
    self.left = parent    


#class Node(object):
  #def __init__(self, data, parent = None, dataNext = None):
    #self.data = data
    #self.parent = parent    
    #self.dataNext = dataNext
    

    
    
    
rootNew = Node(0, None)

#inorder print left, root, right
def printn(root):
  global rootNew
  if root == None:
    return
  printn(root.left)
  
  temp = root
  rootNew.nextD(temp)
  temp.pre(rootNew)
  rootNew = temp
  
  printn(root.right)
		
def printl(root):
  if root == None:
    return
  print root.data
  printl(root.left)


  
  

def main():
  #building the BST
  root = Node(42, None)
  
  root.insert(45)
  root.insert(25)
  root.insert(12)
  root.insert(37)
  root.insert(9)
  root.insert(13)
  root.insert(40)	
  
  #-----
  printn(root)
  printl(rootNew)

	
	
if __name__ == "__main__":
	main()


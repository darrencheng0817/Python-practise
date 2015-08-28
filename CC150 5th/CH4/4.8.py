#You have two very large binary trees: T1, with millions of nodes, and T2, with hun- dreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

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
        
#building the BST (T1)
root = Node(42, None)
root.insert(45)
root.insert(25)
root.insert(12)
root.insert(37)
root.insert(9)
root.insert(13)
root.insert(40)

#building the BST subtree (T2)
roots = Node(12, None)
roots.insert(9)
roots.insert(13)

roots1 = Node(13, None)

t1 = Node(1, Node(2, Node(4, Node(4), Node(5)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
t2 = Node(5, Node(4), Node(5))


#testing
#print root.left.left.parent.parent.right.data

#inorder print left, root, right
def printn(root):
  if root == None:
    return
  printn(root.left)
  print root.data
  printn(root.right)
  

#check the subtree matching, only when the root of T2 matches the node in T1 -> O(n + Km)
def treecheck(T1, T2):
  #both hit the end of the tree
  if T1 == T2 == None:
    return True
  #only one hits the end of the tree
  elif T1 == None and T2 != None:
    return False
  elif T2 == None and T1 != None:
    return False
  #two tree have different data, so T2 is not a
  elif T1.data != T2.data:
    return False
  else:
    #continue checkin both right and left hand side
    return treecheck(T1.right, T2.right) and treecheck(T1.left, T2.left)
  
  
#check the starting point and subtree
def checker(T1, T2):
  #empty tree, then it should return 1
  if T2 == None:
    return True
  if T1 == None:
    return False
  elif T1.data == T2.data:
    return treecheck(T1, T2) 
  else:
    return checker(T1.left, T2) or checker(T1.right, T2)
    
print checker(t1, t2)




#slower approach(in order walk + brute force) -> I would say this method is same as previous one (O(n + Km))
#but using extra memory to store two lists are the overheat
#I think the good point is to insert null in the list to prevent the duplicated nodes cases
list1 = []
list2 = []
def inorder(T1):
  global list1
  if T1 == None:
    list1.extend([None])
    return
  inorder(T1.left)
  list1.extend([T1.data])
  inorder(T1.right) 
  
def inorder2(T1):
  global list2
  if T1 == None:
    list2.extend([None])
    return
  inorder2(T1.left)
  list2.extend([T1.data])
  inorder2(T1.right) 
  
inorder(roots)
inorder2(root)
print list1
print list2#T1
i = 0
while(i < len(list2)):
  if (list2[i] == list1[0]):
    temp1 = 0
    while(temp1 < len(list1)):
      if(list2[temp1] != list1[temp1] or temp1 + i >= len(list2)):
        break
      temp1 += 1
    if temp1 == len(list1):
      print "found"
      break
  i += 1
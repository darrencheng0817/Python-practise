#Implement a function to check if a binary tree is a binary search tree

#1), Inorder walk (left, root, right) and store the element in the list
#2), print the value one by one 
#3), check the size of integer, which should be an increasing order

class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

t = Node(3, Node(2, Node(1)), Node(0))
lista = []

#postorder print left, right, root
def printn(root):
  if root == None:
    return
  printn(root.left)
  printn(root.right)
  print root.data
 
#Inorder walk (left, root, right) 
def store_inorder(node):
  global lista
  if node == None:
    return 
  else:
    store_inorder(node.left)
    lista.append(node.data)
    store_inorder(node.right)
    

def checker(lista):
  flag = 0
  pre = float("-inf")
  for i in lista:
    if flag == 0:
      pre = i
      flag = 1
    else:
      if i < pre:
        print "Not a BST"
        break
      else:
        pre = i
      
store_inorder(t)   
print lista
checker(lista)


    
    
    
    
  

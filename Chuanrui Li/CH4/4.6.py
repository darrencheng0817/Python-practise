#Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

1), this approach seperates the height calculation and balance check (bottom up)
2), better design, create a shortcut for subproblem, if the subtree does is not balance, we return at once, do not follow the original stack call back. -> space cost: O(h) this is the size of the stack, time cost: O(n) T(n) = 2T(n/2) + 1

class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

#def traverse(rootnode):
  #thislevel = [rootnode]
  #while thislevel:
    #nextlevel = list()
    #for n in thislevel:
      #print n.value,
      #if n.left: nextlevel.append(n.left)
      #if n.right: nextlevel.append(n.right)
    #print
    #thislevel = nextlevel

t = Node(1, Node(2, Node(4)), Node(3))


#postorder print left, right, root
def printn(root):
  if root == None:
    return
  printn(root.left)
  printn(root.right)
  print root.data


def height(node):
  if node == None:
    return 0
  else:
    return max(height(node.left), height(node.right)) + 1
  
  
    
def balanced(root):
  if root == None:
    return True
  else:
    return balanced(root.left) and balanced(root.right) and abs(height(root.left) - height(root.right)) < 1
  
haha = balanced(t)
print haha
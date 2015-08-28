#Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists).

#classes
class Nlist(object):
  def __init__(self, data):
    self.data = data
    self.nextNode = None
  def append(self, data):
    new = Nlist(data)
    while self.nextNode != None:
      self = self.nextNode
    self.nextNode = new

class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
      

#Helper functions
#postorder print left, right, root
def printn(root):
  if root == None:
    return
  printn(root.left)
  printn(root.right)
  print root.data

def printl(node):
  while(node != None):
    print node.data
    node = node.nextNode

#def search(root):
    #global result
    #q =Queue()
    #q.enqueue(root)
    #index = 0
    #counter = 0
    #level = 0
    #while(q.isEmpty() == False):
        #key = q.dequeue()  
        ##append the value of key at the end
        #if level == counter+1:
          #result.extend(key)
          #result.extend("!")
          ##reset the counter for the next level
          #index += 1
          #level = math.pow(2, index)
          #counter = 0
        #else:
          #result.extend(key)
        #if key.left != None:
          #q.enqueue(key.left)
        #elif key.right != None:
          #q.enqueue(key.right)
        #if key.left != None or key.right != None:
          #counter += 1
    #return
#1), get the BFS right, done
def BFS(t):
  global result
  q = Queue()
  q.enqueue(t)
  result.extend([t])
  while(q.isEmpty() == False):
    key = q.dequeue() 
    if key.left != None:
      result.extend([key.left])
      q.enqueue(key.left)
    if key.right != None:
      result.extend([key.right])
      q.enqueue(key.right)
      
#2), level break in the linked list
def store_value(result):
  global ans
  counter = 0
  level = 0
  height = 0
  previous = 0
  ans.append([])
  ans[height].extend([result[counter]])
  #iterate the list
  while counter < len(result):
    #check the level
    if counter == level + previous:
      print counter, level
      #increment the height
      height += 1
      ans.append([])
      level = pow(2, height)
      #store the # of elements for the previous level
      previous = counter
    #find the next node in the list
    counter += 1
    if counter == len(result):
      break
    ans[height].extend([result[counter]])
    
    
      
def printlist(elem):
  for i in elem:
    print i.data
    
def print2D(elements):
  # Loop over rows.
  for row in elements:
    print "level"
      # Loop over columns.
    for column in row:
      print column.data
t = Node(1, Node(2, Node(4, Node(4), Node(5)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
#t = Node(1, Node(2, Node(4)), Node(3))

result = []
ans = []


root = Nlist(1)
node1 = Nlist(2)
node2 = Nlist(3)

root.nextNode = node1
node1.nextNode = node2

node2.append(4)
printn(t)
BFS(t)
print  "-------------"
printlist(result)
print  "-------------"
store_value(result)
print  "-------------"
print ans[0][0].data
print ans[1][0].data
print  "-------------"
print2D(ans)


  





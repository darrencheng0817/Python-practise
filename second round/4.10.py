#subtree solutions

#bad approach 
class Node(object):
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

t1 = Node(1, Node(2, Node(4, Node(4), Node(5)), Node(5, Node(4), Node(5))), Node(3, Node(1, Node(4), Node(5)), Node(3, Node(4), Node(5))))
t2 = Node(4, Node(4), Node(5))
list1 = []

def inorder(node):
	global list1
	if node == None:
		list1.extend([node])
		return
	inorder(node.left)
	list1.extend([node.data])
	inorder(node.right)

def subfinder(mylist, pattern):
	pattern = set(pattern)
	return [x for x in mylist if x in pattern]

inorder(t1)
print list1
list3 = list1
list1 = []
inorder(t2)
print list1

print "---"
print subfinder(list3,list1)



	

	






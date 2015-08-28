#subtree solutions

#bad approach -> must include none to guarantee the right result
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

#main for the first method

inorder(t1)
print list1
list3 = list1 # list3 T1
list1 = []
inorder(t2)
print list1 #T2

i = 0
while i < len(list3):
	j = i
	index = 0
	while index < len(list1) and j < len(list3):
		if list1[index] != list3[j]:
			break
		index += 1
		j += 1
	if index == len(list1):
		print "match"
		break
	i+= 1



#Second method -> less space 
def subtree(t1, t2):
	#base
	#t1 and t2 should hit the none node at the same time
	if t1 == t2 == None:
		return True
	elif t1 != None and t2 == None:
		return False
	elif t1 == None and t2 != None:
		return False
	elif t1.data != t2.data:
		return False

	return subtree(t1.right, t2.right) and subtree(t1.left, t2.left)


def tree(t1, t2):
	#based cases
	if t1 == None:
		return False
	if t2 == None:
		return True
	elif t1.data == t2.data:
		return subtree(t1, t2)

	return tree(t1.right, t2) or tree(t1.left, t2) 


print tree(t1, t2)
	

	






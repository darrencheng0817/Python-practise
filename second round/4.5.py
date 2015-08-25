#validate BST
#if no duplicates, we can directly use in order walk


class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right


t = Node(4, Node(2, Node(1), Node(4.4)), Node(9, Node(8), Node(10)))

#tracking the previous variable -> temp buffer
pre = None

def checkBST(node):
	global pre
	if node == None:
		return True
	#checking BST
	if checkBST(node.left) == False:
		return False

	if pre != None:
		if pre > node.data:
			return False

	pre = node.data
	
	if checkBST(node.right) == False:
		return False

	return True

print checkBST(t)
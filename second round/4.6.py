#three cases
#1, if the tree has a right subtree, returning the leftmost node of right subtree
#2, the node is right child of n.parent -> going up and find node is left child of n.parent
#3, the node is left child of n.parent -> return n.parent directly

#find the 'next' node in the binary search tree, following a sequence of in order walk

class Node:
	def __init__(self, data, parent = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def insert(self, data):
		if self.data:
			if self.data > data:
				if self.left is None:
					self.left = Node(data, self)
				else:
					self.left.insert(data)
			elif self.data < data:
				if self.right is None:
					self.right = Node(data, self)
				else:
					self.right.insert(data)
		else:
			self.data = data
					
root = Node(4, None)
root.insert(2)
root.insert(9)
root.insert(1)
root.insert(3)
root.insert(8)
root.insert(15)
	
					
		
#t = Node(4, Node(2, Node(1), Node(3)), Node(9, Node(8), Node(15)))

def leftmost(node):
	while node.left != None:
		node = node.left
	return node

	

def successor(node):
	if node.right != None:
		#case1
		return leftmost(node.right)
	else:
		#case2
		while (node.parent.right == node):
			node = node.parent
			if node.parent == None:
				#case4:
				print "last element"
				return Node("hehe", None)
		#case3
		return node.parent

print successor(root).data 








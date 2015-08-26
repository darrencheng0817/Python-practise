#Common Ancestor:



class Node:
	def __init__(self, data, parent = None, left = None, right = None):
		self.data = data
		self.parent = parent
		self.right = right
		self.left = left

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
root.insert(0)


#if this is a BST , the worst case still O(n)
#using the find method

def find(node1, node2, root):
	#base case
	if root == None:
		return None
	if root.data >= node1.data and root.data <= node2.data:
		return root
	elif root.data <= node1.data and root.data >= node2.data:
		return root


	result1 = find(node1, node2, root.right)
	if result1 != None:
		return result1
	
	result2 = find(node1, node2, root.left)
	if result2 != None:
		return result2


#check the result -> assuming all the nodes are in the BST
#if not, do the checking before the iteration

#result = find(root.left.left, root.right.right, root)
#if result != None:
#	print result.data
#else:
#	print result
	

#if this is a BT , the worst case still O(n)
def cover(root, node):
	if root == None:
		return False
	elif root == node:
		return True
	return cover(root.right, node) or cover(root.left, node)
	
		
	


def common(root, node1, node2):
	if root == None:
		return None
	elif root == node1:
		return node1
	elif root == node2:
		return node2
	
	result1 = cover(root.right, node1)
	result2 = cover(root.right, node2)
	
	#go to diff paths
	if result1 != result2:
		return root
	else:
		if result1 == result2 == False:
			return common(root.left, node1, node2)
		elif result1 == result2 == True:
			return common(root.right, node1, node2)


print common(root, root.left.left, root.left.left.left).data

	
		







#sorted array for unique integer elements to create a binary search tree with minimal height
#the time complexity is O(nlogn)

array = [1, 2, 3, 4, 5, 7, 1000]

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def BST(array, start, end):
	mid = (start + end) / 2
	#Base case
	if start > end:
		return None

	#First 
	root = Node(array[mid])
	#receving the subtree from the last level
	root.left = BST(array, start, mid-1)
	root.right = BST(array, mid+1, end)

	#for this level, the root need to previous calling level
	#bottom up approach
	return root


#inorder left, root, right
def printTree(node):
	#base 
	if node == None:
		return 
	printTree(node.left)
	print node.data
	printTree(node.right)

node = BST(array, 0, len(array)-1)
printTree(node)


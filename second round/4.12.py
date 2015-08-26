#paths of sum
class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.right = right
		self.left = left

t = Node(4, Node(2, Node(1), Node(3)), Node(9, Node(8), Node(15)))

def printN(node):
	if node == None:
		return
	printN(node.left)
	print node.data
	printN(node.right)

def depth(node):
	if node == None:
		return 0
	else:
		return max(depth(node.right), depth(node.left)) + 1

path = [0]*depth(t)


def printlist(level, path):
	sum1 = 9
	psum = 0
	index = level
	while index >= 0:
		psum += path[index]
		if psum == sum1:
			#print function
			index2 = index
			while index2 <= level:
				print path[index2],
				index2 += 1
		
		index -= 1


#path sum: -> this is like a stack, the top level recursion call, will replace the 
#data in the path

def pathsum(node, level, path):
	#base case
	
	if node == None:
		return
	#assign the value 
	path[level] = node.data
	printlist(level, path)
	
		
	pathsum(node.right, level+1, path)
	pathsum(node.left, level+1, path)
		


pathsum(t, 0, path)











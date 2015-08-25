#check balance
class Node:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

t = Node(1, Node(2, Node(4), Node(4)), Node(3, Node(4)))

def height(node):
	if node == None:
		return 0
	return max(height(node.right), height(node.left)) + 1


def balance(node):
	if node == None:
		return True
	else:
		return balance(node.left) and balance(node.right) and abs(height(node.left) - height(node.right)) < 1


print balance(t)







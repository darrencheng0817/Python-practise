#remove duplicates
#-> hashtable is O(n) with extra space
#-> brute force no extra space


Class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextNode = none

	def printNode(root):

	while root != None:
		print root.data
		root = root.nextNode


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)


node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = None



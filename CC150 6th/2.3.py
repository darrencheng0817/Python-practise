#Delete Middle Node -> only one access
#Return Kth to last
class Node:
	def __init__(self, data):
		self.data = data
		self.nextNode = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(7)
node5 = Node(8)


node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5

def deleteNode(node):
	node.data = node.nextNode.data
	node.nextNode = node.nextNode.nextNode

def printll(node):
	while node != None:
		print node.data
		node = node.nextNode


deleteNode(node2)
printll(node1)






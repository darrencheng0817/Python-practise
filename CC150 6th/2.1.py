#remove duplicates
#-> hashtable is O(n) with extra space
#-> brute force no extra space


class Node:
	def __init__(self, data):
		self.data = data
		self.nextNode = None

	def printNode(self):
		while self != None:
			print self.data,
			self = self.nextNode


node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
node4 = Node(1)
node5 = Node(1)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5


#main -> implement none space cost
index1 = node1
while index1 != None:
	pre = index1
	index2 = index1.nextNode
	while index2 != None:
		#duplicates, pre non-change, index2 change
		if index1.data == index2.data:
			pre.nextNode = index2.nextNode
			index2 = index2.nextNode
		#pre change, index2 change
		else:
			pre = index2
			index2 = index2.nextNode
			
	index1 = index1.nextNode


node1.printNode()

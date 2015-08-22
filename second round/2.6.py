#Palindrome
#check the ll is a Palindrome

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

def printll(node):
	while node != None:
		print node.data
		node = node.nextNode

#main source code
#covert into a list and then check the palin
list1 = []

def palin(node1):
	#covert into a list 
	while node1 != None:
		list1 = list1 + [node1.data]
		node1 = node1.nextNode

#checking 
if list1== list1[::-1]:
	print "ok"
else:
	print "No"
	





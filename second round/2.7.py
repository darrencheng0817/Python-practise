#intersection of two list
#ex:
#3->1->5->9
#			\
#			  7->2->1 
#			/
#	   4->6
# intersection is 7, we only compare the reference not the value

class Node:
	def __init__(self, data):
		self.data = data
		self.nextNode = None

#first linked list
node1 = Node(3)
node2 = Node(1)
node3 = Node(5)
node4 = Node(9)
node5 = Node(7)
node6 = Node(2)
node7 = Node(1)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7

#second linked list
node8 = Node(4)
node9 = Node(6)

node8.nextNode = node9
node9.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7


def printll(node):
	while node != None:
		print node.data
		node = node.nextNode


#find the diff of length between two lists
def counter(node1, node2):
	start1 = node1
	start2 = node2
	counter1 = 0
	counter2 = 0
	while node1 != None:
		counter1 += 1
		node1 = node1.nextNode

	while node2 != None:
		counter2 += 1
		node2 = node2.nextNode

	#distinct two lines
	if node1 != node2:
		print "No"
		return

	diff = counter1 - counter2
	if diff > 0:
		while diff > 0:
			start1 = start1.nextNode
			diff -= 1

		while start1 != None:
			if start1 == start2:
				print "yes 1", start1
				return
			#increment the data
			start1 = start1.nextNode
			start2 = start2.nextNode

	elif diff < 0:
		diff = abs(diff)
		while diff > 0:
			start2 = start2.nextNode
			diff -= 1

		while start2 != None:
			if start2 == start1:
				print "yes 2", start2
				return
			#increment the data
			start1 = start1.nextNode
			start2 = start2.nextNode
	else:
		while start2 != None:
			if start2 == start1:
				print "yes 3", start2
				return
			#increment the data
			start1 = start1.nextNode
			start2 = start2.nextNode



counter(node8, node1)








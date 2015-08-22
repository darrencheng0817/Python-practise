#partition
#3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1, partition is 5
#3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class Node:
	def __init__(self, data):
		self.data = data
		self.nextNode = None


node1 = Node(3)
node2 = Node(5)
node3 = Node(8)
node4 = Node(5)
node5 = Node(10)
node6 = Node(2)
node7 = Node(1)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7

def printn(node):
    while(node != None):
        print node.data,
        node = node.nextNode




list1 = [] 
def convert_ll_to_l(node, input1):
	global list1
	while node != None:
		if input1 > node.data:
			list1 = [node.data] + list1
		else:
			list1 = list1 + [node.data]
		node = node.nextNode
	print list1


def convert_l_to_ll():
	global list1
	node1 = Node(list1[0])
	first = node1
	for i in range(1, len(list1)):
		node2 = Node(list1[i])
		first.nextNode = node2
		first = node2
	return node1



convert_ll_to_l(node1, 5)
printn(convert_l_to_ll())



class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def printN(self):
		while self != None:
			print self.data,
			self = self.next



root = Node(7, Node(1, Node(3, Node(4, Node(5, Node(9, None))))))

#root.printN()

def partition(root, newNode, num):
	tail = head = newNode 
	while root != None:
		if newNode.data == None:
			newNode.data = root.data
			
		elif root.data >= num:
			tail.next = Node(root.data)	
			tail = tail.next
			
		elif root.data < num:
			temp = Node(root.data)
			temp.next = head
			head = temp
			
		root = root.next
		
	#final stage
	tail.next = None
	return head
	
def init(root):
	newNode = Node()
	num = 3
	return partition(root, newNode, num)
	
res = init(root)
#print res
res.printN()




	
class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

	def printN(self):
		while self != None:
			print self.data,
			self = self.next



root = Node(1, Node(2, Node(3, Node(4, None))))

#iteration
def reverse1(node):
	pre = node
	cur = node.next
	later = node.next.next
	pre.next = None
	while cur != None:
		cur.next = pre
		pre = cur
		cur = later
		if cur == None:
			break
		later = later.next

	return pre
	
#recursion
def reverse2(pre, cur, later):
	cur.next = pre
	if later == None:
		return cur
	return reverse2(cur, later, later.next)
		

		
def recursion(node):
	pre = node
	cur = node.next
	later = node.next.next
	pre.next = None
	return reverse2(pre, cur, later)	


#pre = reverse1(root)
#pre.printN()
#print "----"
pre = recursion(root)
pre.printN()


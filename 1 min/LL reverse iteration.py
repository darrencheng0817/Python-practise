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
#pre = recursion(root)
#pre.printN()


#-------------------- better solution to solve this problem, general logic is same

#this code deal with special cases and general cases together
def reverse3(head):
	pre = None
	while head != None:
		#change linking
		later = head.next
		head.next = pre
		#update -> head and later are in the same position before changing the links
		pre = head
		head = later
		
	return pre
	
#-------------------------
#pre = reverse3(root)
#pre.printN() 

#recursion method
#origin approach
#-> (pre -> curr),(curr -> later),(later -> later.next)
#improvement
#-> (pre -> curr), (curr-> later)

def reverse4(cur, pre):
	while cur == None:
		return pre
	later = cur.next
	cur.next = pre
	return reverse4(later, cur)	
	

def recursion2(root):
	return reverse4(root, None)

#main -------------------------
pre = recursion2(root)
pre.printN()



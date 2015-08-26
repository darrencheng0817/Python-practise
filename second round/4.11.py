#Implement a BST
#function -> insert, delete, find and getRandomNode()
#delete is similar to the succecer?? -> wll be Implement later
import random
counter = 0

class Node:
	def __init__(self, data, id, left = None, right = None):
		global counter 
		counter += 1
		self.data = data
		self.id = id
		self.left = left
		self.right = right

	def insert(self, data, id):
		if self.data:
			if self.data > data:
				if self.left == None:
					self.left = Node(data, id)
				else:
					self.left.insert(data, id)
			elif self.data < data:
				if self.right == None:
					self.right = Node(data, id)
				else:
					self.right.insert(data, id)
		else:
			self.data = data

	def find(self, data):
		if self == None:
			return None
		if self.data == data:
			print 'found'
			return data
		elif self.data > data and self.left != None:
			return self.left.find(data)
		elif self.data < data and self.right != None:
			return self.right.find(data)
		return None
		
		
	def findID(self, id):
			if self == None:
				return 
			if self.id == id:
				print self.data
				return 
			if self.left != None:
				self.left.findID(id)
			if self.right != None:
				self.right.findID(id)
			
	#delete cases do not handle yet
	def getRandomNode(self):
		global counter
		id = random.randrange(0, counter, 1)
		self.findID(id)

#inorder left, root, right
def printTree(node):
	#base 
	if node == None:
		return 
	printTree(node.left)
	print node.data
	printTree(node.right)

root = Node(4, 0)
root.insert(2, 1)
root.insert(9, 2)
root.insert(1, 3)
root.insert(3, 4)
root.insert(8, 5)
root.insert(15, 6)
root.insert(0, 7)


#printTree(root)
root.find(15)
root.getRandomNode()
print counter




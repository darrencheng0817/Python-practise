#Stack min

list1 = []
class Stack:
	def __init__(self):
		global list1
		list1 = [0]*10
		self.counter = 0
		self.min = float("inf")

	def push(self, item):
		global list1
		#set min
		if self.min > item:
			list1[-self.counter-1] = item
			self.min = item
		else:
			list1[-self.counter-1] = self.min
		#set value
		list1[self.counter] = item
		self.counter += 1

	def pull(self):
		global list1
		#pull value
		list1[self.counter-1] = 0
		list1[-self.counter] = 0

		#reset min
		self.counter -= 1
		self.min = list1[-self.counter]

	def min1(self):
		global list1
		print list1[-self.counter]

stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(2)
print list1
stack.pull()
stack.push(0.5)
stack.min1()
print list1







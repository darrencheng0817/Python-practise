#Three in one
list1 = [0]*9

class Stack:
	def __init__(self, stackN):
		global list1
		if stackN == 1:
			self.stackN = 1
			self.counter = 0
		elif stackN == 2:
			self.stackN = 2
			self.counter = 0
		elif stackN == 3:
			self.stackN = 3
			self.counter = 0

	def pop1(self):
		global list1
		if self.stackN == 1:
			print self.counter
			if self.counter < 0:
				print "hhe"
				return False
			list1[self.counter-1] = 0
			self.counter -= 1
		elif self.stackN == 2:
			
			if self.counter < 3:
				return False
			list1[self.counter+2] = 0
			self.counter -= 1
		elif self.stackN == 3:
			
			if self.counter < 6:
				return False
			list1[self.counter+5] = 0
			self.counter -= 1


	def push(self,item):
		global list1
		if self.stackN == 1:
			if self.counter > 3:
				return False
			list1[self.counter] = item
			self.counter += 1
		elif self.stackN == 2:
			if self.counter > 6:
				return False
			list1[self.counter+3] = item
			self.counter += 1
		elif self.stackN == 3:
			if self.counter > 9:
				return False
			list1[self.counter+6] = item
			self.counter += 1


stack1= Stack(1)

stack1.push(3)
stack1.push(3)
stack1.push(1)
stack1.pop1()


stack2= Stack(2)
stack2.push(4)
stack2.push(4)
stack2.push(5)


print list1




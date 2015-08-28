
#sorted stack, the biggest element is on the top

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self, item):
		return self.items.append(item)

	def pop1(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]


def sort(s1, s2):
	#s1 -> data stack, s2 -> final stack
	s2.push(s1.pop1())
	while not s1.isEmpty():
		#pull the value from s1 to s2
		temp = s1.pop1()
		while temp < s2.peek():
			s1.push(s2.pop1())
			if s2.isEmpty():
				break
		s2.push(temp)

#this is the stack
s1 = Stack()
s1.push(8)
s1.push(5)
s1.push(7)
s1.push(10)
s1.push(11)


s2 = Stack()
sort(s1, s2)
print s1.items, s2.items




		







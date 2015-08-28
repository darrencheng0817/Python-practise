#Using two stack to create a queue

#stack -> last in first out
#queue -> first in first out


#performance improvement -> only reverse the stack when the dequeue happens

stack1 = []
stack2 = []

def enqueue(item):
	global stack1
	stack1.append(item)

def dequeue():
	global stack1, stack2
	if len(stack2) == 0:
		while len(stack1) != 0:
			stack2.append(stack1.pop())
			if len(stack2) == 0:
				return False
		return stack2.pop()
	else:
		return stack2.pop()


enqueue(1)
enqueue(2)
enqueue(3)
print dequeue()
print dequeue()
print dequeue()
enqueue(4)
print dequeue()

print stack1, stack2









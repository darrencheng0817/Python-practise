#three in one

#list of list, each sub-list is a sub-stack
#functions: push(), pull(), popat()
##Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

#assumption is that: three sub-stack, three elements in sub-stack
stack = [[None] * 3 for i1 in range(3)]

indx, indy = 0, 0

def push(item):
	global stack, indx, indy
	found = 0
	for i in range(0, len(stack)):
		for j in range(0, len(stack[i])):
			if stack[i][j] == None:
				stack[i][j] = item
				indx, indy = i, j
				found = 1
				break
		if found == 1:
			break

def pull():
	global stack, indx, indy
	stack[indx][indy] = None
	if indy != 0:
		indy -= 1
	elif indx != 0:
		indx -=1
		indy = 2
	else:
		return 

def popAt(index):
	indx = index/3
	indy = index%3
	stack[indx][indy] = None
	
	
	


push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
pull()
pull()
push(5)
push(6)
popAt(0)
push(6)


print stack













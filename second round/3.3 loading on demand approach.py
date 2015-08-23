#Imagine a (literal) stack of plates. If the stack gets too high, it might topple. There- fore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOf- Stacks should be composed of several stacks, and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
#FOLLOW UP
#Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.


#1), Create a stack by list and create a list of list
#2), When hit the limit of the list, 
#3),

stack = [[0]*3]
index1 = 0
row = 0

def push1(num):
    global stack
    global index1
    global row
    if(index1 == 3):
    	stack.append([0]*3)
	index1 = 0
	row += 1
    stack[row][index1] = num
    index1 += 1

def pop1(num):
    global stack
    global row    
    global index1
    if(index1 == 0 and row == 0):
    	print "died"
    	return
    if(index1 == 0 and row != 0):
	row -= 1
	index1 = 3
    if(stack[row][index1-1] != num):
	print "cannot do it"
	return    
    stack[row][index1-1] = 0
    index1 -= 1
    
def popAt(indexk):
    global stack
    global row    
    global index1    
    #check the size first
    #convert the indexk to row and index1
    print row, index1
    if indexk > row*3 + index1:
	print "error"
	return
    else:
	x = indexk/2
	y = indexk%2
	print x, y
	if indexk < 3:
	    stack[x][y] = 0 
	else:
	    stack[x][y-1] = 0
	    
	

push1(1)
push1(2)
push1(3)
push1(4)
push1(5)
push1(6)
push1(7)
pop1(7)
pop1(6)
popAt(3)



print stack
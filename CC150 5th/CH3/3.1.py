# Describe how you could use a single array to implement three stacks.

#since array size is fixed, we can divide the array into three parts and each partition is a stack

#better way: loading on demand, the array has been divided into same pages contains k cells and each cell will have a identifer in the first cell for k cells. allocates pages by pages

list = [0]*6
index1 = 0
index2 = 3
def push1(num):
    global index1
    if(index1 == 3):
    	print "died"
    	return
    list[index1] = num
    index1 += 1

def push2(num):
    global index2
    if(index2 == 6):
    	print "died"
        return
    list[index2] = num
    index2 += 1

def pop1(num):
    global index1
    if(index1 == 0):
    	print "died"
    	return
    if(list[index1-1] != num):
	print "cannot do it"
	return    
    list[index1-1] = 0
    index1 -= 1

def pop2(num):
    global index2
    if(index2 == 3):
    	print "died"
    	return
    if(list[index2-1] != num):
	print "cannot do it"
	return
    list[index2-1] = 0
    index2 -= 1
    
push1(1)
push2(2)
push1(17)
push1(11)
pop2(2)


print list

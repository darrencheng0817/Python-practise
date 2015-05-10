# Describe how you could use a single array to implement three stacks.

#since array size is fixed, we can divide the array into three parts and each partition is a stack

#better way: loading on demand, the array has been divided into same pages contains k cells and each cell will have a identifer in the first cell for k cells. allocates pages by pages

#first we divide the whole stack into two parts and then top part to store all min elements for each stage
#second, bottom part to store actual stack value

list = [0]*6
index1 = 0
index2 = 5
#define a positive infinite
minimum = float("inf")
def push1(num):
    global minimum
    global index1
    if(index1 == 3):
    	print "died"
    	return
    list[index1] = num
    index1 += 1
    if num < minimum:
	minimum = num
	push2(num)
    else:
	push2(minimum)

def pop1(num):
    global minimum
    global index1
    if(index1 == 0):
    	print "died"
    	return
    if(list[index1-1] != num):
	print "cannot do it"
	return    
    list[index1-1] = 0
    index1 -= 1
    pop2()
	

def push2(num):
    global index2
    if(index2 == 2):
    	print "died"
        return
    list[index2] = num
    index2 -= 1

def pop2():
    global index2
    if(index2 == 5):
    	print "died"
    	return
    list[index2+1] = 0
    index2 += 1
    
def min():
    print "the min is: " + str(list[index2+1])
    
push1(111111)
push1(111)
push1(17)
pop1(17)
min()





print list
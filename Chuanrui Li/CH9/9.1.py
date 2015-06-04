#a child is running up a staircase with n steps, and can hop either 1 step, 2 step, 3 step at a time
#Implement a method to count how many possible ways the child can run up the stairs



def stair(n, counter):
    if n == 0:
    	counter[0] += 1
    	return 
    if n < 1:
	return
    else:
	stair(n-1, counter)
	stair(n-2, counter)
	stair(n-3, counter)
 
#every subproblem will return the result to the upper level problem
#using the memorization method
def staircase(n, list2):
    if n == 0:
	return 1
    if n < 1:
	return 0
    if list2[n] != 0:
	return list2[n]	
    else:
	return staircase(n-1, list2) + staircase(n-2, list2) + staircase(n-3, list2)
	

def main():
    n = 6
    list1 = [0]
    stair(n, list1)
    print list1
    
    #checking the value
    list2 = [0]*(n+1)
    print staircase(n, list2)
    

if __name__ == "__main__":
    main()







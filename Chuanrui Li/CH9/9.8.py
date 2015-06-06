#Write a method that returns all subsets of a set.
#for set(0) --> []
#for set(1) -->  []+ [1] = [[], [1]]
#for set(2) -->  [[], [1]] + [2], [1, 2]= [[], [1], [2], [1, 2]]
from copy import deepcopy
result = [[]]

def subset(list1):
	global result
	step = []
	
	for i in range(0, len(list1)):
		#print "-------------"
		step = deepcopy(result)
		#this is the new value
		for j in result:
			j.extend([list1[i]])
		
		#the older value for the last level
		#using a trick, adding a empty list
		result = step[:] + result
	        #print result
		step = []
		i -= 1

def main():
	list1 = [1, 2, 3]
  	subset(list1)
  	print "/////////////////-----answer:"
  	print result

    

if __name__ == "__main__":
	main()










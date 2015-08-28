#Describe an algorithm to find the largest 1 million numbers in 1 billion numbers. Assume that the computer memory can hold all one billion numbers.

#approach: quick select: find the nth smallest number in the array

def ranSelect(list1):
	print list1
	counter = 0
	list1_hehe = []
	list1_haha = []
	for i in range (1, len(list1)):
		if list1[i] < list1[0]:
			list1_hehe += [list1[i]]
			counter+=1
		else:
			list1_haha += [list1[i]]
 
	
	return counter, list1_hehe, list1_haha, list1[0]

def quickSelect(list1, start, end, pos):
	index, Slist, Blist, result = ranSelect(list1)
	print index, pos
	if index == pos:
		return result
	if index > pos:
		return quickSelect(Slist, 0, len(Slist), pos)
	else:
		return quickSelect(Blist, 0, len(Blist), pos-index-1)
	



def main():
	list1 = [26, 19, 35, 29, 33, 12, 22]	
	print quickSelect(list1, 0, len(list1), 6)	
	#print ranSelect(list1)
		
if __name__ == "__main__":
	main()


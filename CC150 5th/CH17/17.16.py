#find the second smallest element of the list, can only iterate once and using the recursion

def secSmall(list1, list2, index):
	if index == len(list1):
		return list2
	else:
		small = min(list1[index])
		if small < max(list2[0], list2[1]):
			if list2[0] == max(list2[0], list2[1]):
				list2[0] = small
			else:
				list2[1] = small			
		
		return secSmall(list1, list2, index+1)
		


def main():
	list1 = [[2, -8], [3], [4, -10]]
	list2 = [float('inf'), float('inf')]
	#for i in list1:
		#small = min(i)
		#if small < max(list2[0], list2[1]):
			#if list2[0] == max(list2[0], list2[1]):
				#list2[0] = small
			#else:
				#list2[1] = small	
	#print list2
	#list2 = [float('inf'), float('inf')]
	print secSmall(list1, list2, 0)
	
	
if __name__ == "__main__":
	main()


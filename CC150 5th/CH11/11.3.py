#Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
#EXAMPLE:
#Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
#Output: 8 (the index of 5 in the array)

#1,) sorted rotated array -> BS

def Bsearch(list1, start, end, digit):
	#return for the error cases:
	if start > end:
		return -1
	mid = (start + end) / 2
	if list1[mid] == digit:
		return mid
	#big cas1
	#15, digit, list1[mid], 25, 1 ....
	elif list1[mid] > digit and digit > list1[-1]:
		return Bsearch(list1, start, mid-1, digit)
	#15, list1[mid], 25, 1 digit,14
	elif list1[-1] >= digit and list1[mid] > list1[-1]:
		return Bsearch(list1, mid+1, end, digit)
	elif list1[mid] > digit and list1[mid] <= list1[-1]:
		return Bsearch(list1, start, mid-1, digit)
	
	#big case2
	#15, digit, 25, 1 ,list1[mid], 14
	elif list1[-1] < digit and list1[mid] <= list1[-1]:
		return Bsearch(list1, start, mid-1, digit)
	#15, ... 25, 1 ,list1[mid], digit, 14	
	elif digit > list1[mid] and digit <= list1[-1]:
		return Bsearch(list1, mid+1, end, digit)
	elif list1[mid] < digit and list1[mid] > list1[-1]:
		return Bsearch(list1, mid+1, end, digit)
	return -1

def main():
	list1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	digit = 14
	print Bsearch(list1, 0, len(list1), digit)
	

if __name__ == "__main__":
	main()




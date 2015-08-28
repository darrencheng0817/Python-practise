#Binary search -> only for the sorted array
#time complexity -> O(logn)

array = [1, 2, 3, 4, 5]

def BST(array, start, end, value):
	mid = (start + end) / 2
	if start > end:
		print "None"
		return 
	if array[mid] == value:
		print mid
		return 
	elif array[mid] > value:
		BST(array, start, mid-1, value)
	elif array[mid] < value:
		BST(array, mid+1, end, value)





BST(array, 0, len(array)-1, 3)






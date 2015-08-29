#Binary search -> only for the sorted array
#time complexity -> O(logn)

array = [1, 2, 3, 4, 5]

def BS(array, start, end, value):
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

BS(array, 0, len(array)-1, 3)

#Iteration method for the binary search
def BS2(array, value):
	start = 0
	end = len(array) - 1

	while start <= end:
		mid = (start + end)/2
		if array[mid] == value:
			return mid
		elif array[mid] > value:
			end = mid - 1 
		elif array[mid] < value:
			start = mid + 1
	return None

print BS2(array, 5)






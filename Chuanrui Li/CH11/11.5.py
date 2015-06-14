#Given a sorted array of strings which is interspersed with empty strings, 
#write a method to find the location of a given string

#1,) first, deal with sorted array of string -> BT
#2,) second,deal with the empty strings

def Bsearch(list1, start, end, value):
	if (start > end or start < 0 or end >= len(list1)):
		return -1
	mid = (start + end)/2
	if list1[mid] == value:
		return mid
	#handle the empty space for searching
	elif list1[mid] != " ":
		if list1[mid] > value:
			return Bsearch(list1, start, mid-1, value)
		elif list1[mid] < value:
			return Bsearch(list1, mid+1, end, value)
	else:
		if mid >= len(list1) - 1:
			return Bsearch(list1, start, end-1, value)
		elif mid == start == 1:
			return Bsearch(list1, start-1, end, value)
		else:
			return Bsearch(list1, start+1, end, value)

	return -1


def main():
	list2 = ["a", "b", "c", "d"]
	list1 = [" ", " ", " ", "a", " ", "b",  " ", "c",  " ",  " ", "d", " "]
	value = "a"
	print Bsearch(list1, 0, len(list1)-1, value)

  
  

if __name__ == "__main__":
	main()




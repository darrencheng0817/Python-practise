#Given a matrix in which each row and each column is sorted, 
#write a method to find an element in it.

#1), BS on diagonal line of the matrix
#2), recursive do that on the rest of the part

#this is for multi-dimension slicing
import numpy as np
from copy import deepcopy

def Bsearch(list1, start, end, digit):
	#return for the error cases:
	if start > end:
		return end, start
	mid = (start + end) / 2
	if list1[mid][mid] == digit:
		return mid, mid
	elif list1[mid][mid] > digit:
		return Bsearch(list1, start, mid-1, digit)
	elif list1[mid][mid] < digit:
		return Bsearch(list1, mid+1, end, digit)
	

def find_num(list1, num):
	start = 0
	end = len(list1) - 1
	start, end = Bsearch(list1, start, end, num)
	#print start, end
	if np.array(list1)[:end, end:] != None:
		# print "------------"
		# print np.array(list1)[:end, end:]
		# print start, end, len(np.array(list1)[:end, end:])
		print "$$$$$$$$$$$$$$$$$$"
		newList = deepcopy(np.array(list1)[:end, end:])
		start, end = Bsearch(np.array(list1)[:end, end:], 0, end-1, num)
		if start == end:
			return start
		print "---------------"
		if newList != None:
			print end
			print newList
			start, end = Bsearch(np.array(newList)[:end, end:], 0, end-1, num)
			if start == end:
				
				print start
				return start


		#another half of the table
		#start, end = Bsearch(np.array(list1)[end:, :end], 0, end-1, num)
	#print Bsearch(list1, start, end, num)
	
	#while start < end:
		#start, end = Bsearch(list1, start, end, num)
		
	


def main():
	list1 = [[15, 20, 70, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
	num = 85
	
	print find_num(list1, num)
	

if __name__ == "__main__":
	main()




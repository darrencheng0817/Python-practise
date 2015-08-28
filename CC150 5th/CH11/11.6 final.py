#Given a matrix in which each row and each column is sorted, 
#write a method to find an element in it.

#1), BS on diagonal line of the matrix
#2), recursive do that on the rest of the part

#this is for multi-dimension slicing
import numpy as np
from copy import deepcopy

end_point = 0
flag = True

def Bsearch(list1, start, end, digit):

	#for the multi-rows, we need to do the diagonal search
	#return for the error cases:	
	if start > end:
		return end, start
	mid = (start + end) / 2
	#print start, end, list1
	if list1[mid][mid] == digit:
		
		return mid, mid
	elif list1[mid][mid] > digit:
		return Bsearch(list1, start, mid-1, digit)
	elif list1[mid][mid] < digit:
		return Bsearch(list1, mid+1, end, digit)

	
def find_num1(list1, num, start, end):
	global end_point
	global flag
	#check the empty list input --> does not work
	# if list1.size == 0:
	# 	return None
	if len(list1) == 0:
		#print "here"
		return None
	else:
		start, end = Bsearch(list1, start, end, num)
		if start == end:
			print "FFFFFFOOOUND"
			return start, end		
		#print start, end
		#check the list is empty or not
		if np.array(list1)[:end, end:].size != 0:
			print "$$$$$$$$$$$$$$$$$$"
			newList = deepcopy(np.array(list1)[:end, end:])
			
			#for single row we need to do the linear search--> still have a problem for 6*6
			if len(newList) == end_point:
				if list1[end_point-1][end_point] == num:
					return end_point-1, end_point
				else:
					flag = False
			if flag == True:
				find_num1(newList, num, 0, end-1)
			else:
				flag = True
		#another half
		if np.array(list1)[end:, :end].size != 0:
			print "#################"
			newList = deepcopy(np.array(list1)[end:, :end])
			#print newList
			
			
			#deal with 100
			# for single row we need to do the linear search--> still have a problem
			if len(newList) == 1 and len(newList[0]) == end_point:
				#print "hehehe"
				if list1[end_point][end_point-1] == num:
					return end_point, end_point-1
				else:
					return None
			
			find_num1(newList, num, 0, end-1)			
			
			
		


def main():
	global end_point	
	list1 = [[15, 20, 70, 85], [21, 35, 81, 90], [30, 55, 95, 105], [40, 80, 100, 120]]
	
	end_point = len(list1)-1
	num = 100
	print find_num1(list1, num, 0, len(list1) - 1)
	

if __name__ == "__main__":
	main()




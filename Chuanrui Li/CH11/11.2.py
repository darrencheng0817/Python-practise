#Write an algorithm to print all ways of arranging eight queens on an 8*8 chess board so that none of them 
#share the same row, column or diagonal. In this case, "diagonal" means all diagnals, not just the two that 
#bisect the board

#we need to have a check 
#100   100 010     001
#010   001 100 ..  100 ...
#001   010 001     010
#i=0       i=1     i=2
#NOTE: first one is not right

# [evaluate 9.9.py] ---> answer
# --------------------
# [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
# --------------------
# [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
# --------------------
# [[0, 0, 1], [0, 1, 0], [1, 0, 0]]



queens = []

#checking the position has already occupied
def checking (row, col):
	global queens

	#first time, the list is empty
	if not queens:
		return True
	else:
		for i in queens:
			if i[0] == row or i[1] == col:
				return False
			if (i[0] - row) == (i[1] - col):
				return False
	return True

def result(list1, row, col):
	#global declaration
	global queens
	global counter

	if row == 3:
		print "--------------------"
		print list1
		#counter	+= 1 
		#list1 = [ [ 0 for i in range(3) ] for j in range(3) ]
		return
	else:
		#check the row, cow
		#check all the col for that row
		i = 0
		while i < col:
			if(checking(row, i)):
				#updating the queens' position
				queens = queens + [(row, i)]
				#updating the list1 
				list1[row][i] = 1
				#finished, keep checking the next row 
				#and restart the col from 0 again
				result(list1, row+1, col)
				#remove past data
				queens.remove((row, i))
				list1[row][i] = 0
				#print row, col		
			i += 1


def main():
	row = 3
	col = 3
	list1 = [ [ 0 for i in range(3) ] for j in range(3) ]
	#print list1
 	result(list1, 0, col)

  
  

if __name__ == "__main__":
	main()




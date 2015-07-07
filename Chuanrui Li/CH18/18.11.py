#Imagine you have a square matrix, where each cell is filled with either black or white. 
#Design an algorithm to find the maximum subsquare such that all four borders are filled with black pixels.

matrix = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]


#def issquare():
	
def issquare(Hstart, Hend, Vstart, Vend):
	#top, bottom, right, left
	print "------------------------"
	#print Hstart, Hend, Vstart, Vend
	result = 1
	for i in range(Hstart, Hend+1):
		for j in range(Vstart, Vend+1):
			#print matrix[i][j]
			#print (i, j)
			if matrix[i][j] == 0:
				#print "heheh"
				#print i, j, matrix[i][j]
				if i != 0 and j!= 0 and i != Hend and j != Vend:
					continue
				else:
					result = 0
					break
	if result == 0:
		return False
	else:
		
		return True
	


def main():
	global matrix
	result = False
	#2, 1, 0
	for outer in range(len(matrix)-1, 0, -1):
		#assume the outer = 2
		#print outer
		Hinner = outer
		while Hinner <= len(matrix)-1:
			#this is the result
			Vinner = 1
			while Vinner <= len(matrix)-1:
				result = issquare(Hinner-1, Hinner, Vinner-1, Vinner)
				if result == True:
					#Find a square, do not need to keep checking
					break
				Vinner += 1
			Hinner += 1
			if result == True:
				break		
		if result == True:
			break			
	print outer+1	
			

		
if __name__ == "__main__":
	main()
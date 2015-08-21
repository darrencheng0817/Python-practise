#Zero matrix
#identify the zero and set boolean for the zero place

matrix = [[1, 2, 3], [4, 2, 6], [7, 8, 9], [10, 11, 0]]

def matrix1():
	global matrix
	N = len(matrix) 
	M = len(matrix[0])
	for i in range(0, N):
		for j in range(0, M):
			if matrix[i][j] == 0:
				#column
				matrix[i][0] = 'False'
				#row
				matrix[0][j] = 'False'

	#print matrix

def newM():
	global matrix
	#Column
	for i in range(0, len(matrix[0])):
		if matrix[0][i] == 'False':
			for j in range(0, len(matrix)):
				matrix[j][i] = 0
	#Row
	for i in range(0, len(matrix)):
		if matrix[i][0] == 'False':
			for j in range(0, len(matrix[0])):
				matrix[i][j] = 0
	print matrix

	
 


matrix1()
newM()
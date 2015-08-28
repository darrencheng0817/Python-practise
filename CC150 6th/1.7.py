#Rotate Matrix
#rotate by index

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]

def matrix1():
	global matrix
	end = len(matrix)
	#how many level
	for i in range(0, end/2):
		end = end - i
		#for each level
		for j in range(0, end-1-i):
			print j, end-1
			print matrix[j+i][end-1], matrix[end-1][end-1-j], matrix[end-1-j][i], matrix[i][j+i]

			temp = matrix[j+i][end-1]
			matrix[j+i][end-1]= matrix[end-1][end-1-j]
			matrix[end-1][end-1-j] = matrix[end-1-j][i]
			matrix[end-1-j][i] = matrix[i][j+i]
			matrix[i][j+i] = temp
		
	print matrix

matrix1()
#Rotate Matrix
#rotate by index

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]

def matrix1():
	global matrix
	end = len(matrix)
	for i in range(0, end/2):
		for j in range(i, end-1-i):
			temp = matrix[j][end-1-i]
			matrix[j][end-1-i] = matrix[end-1-i][end-1-i]
			matrix[end-1-i][end-1-j-i] = matrix[end-1-j-i][0]
			matrix[end-1-j-i][0] = matrix[0][j]
			matrix[0][j] = temp
		
	print matrix

matrix1()
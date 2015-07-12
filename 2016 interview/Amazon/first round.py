# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

#read the data
data = sys.stdin.readlines()
length = int(data[0])
def helper(line):
    line = line.split()
    line = map(lambda s:int(s), line)
    return line
matrix = map(helper, data[1:])

def matrix_process(matrix, length):
    for i in range(length):
        if len(matrix[i]) != length:
            print "ERROR"
            return
    for layer in range(0, length/2):
        first = layer
        last = length -layer -1
        #initialize the value 
        top = matrix[first][first]
        left = matrix[last][first]
        bottom = matrix[last][last]
        right = matrix[first][last]
        for inner in range(first, last):
            diff = inner - first
            
            #shift the top
            temp = matrix[first][inner+1]
            matrix[first][inner+1] = top
            top = temp
            
            #shift the left
            temp2 = matrix[last - diff -1][first]
            matrix[last - diff -1][first] = left
            left = temp2
            
            #shift the bottom
            temp3 = matrix[last][last - diff -1]
            matrix[last][last - diff -1] = bottom
            bottom = temp3
            
            #shift the right
            temp4 = matrix[inner+1][last]
            matrix[inner+1][last] = right
            right = temp4
         
    for i in range(0, len(matrix)):   
        for j in range(0, len(matrix[i])):
            print str(matrix[i][j]),
        print

matrix_process(matrix, length)
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

# 1), find all the elements in the MxN matrix is 0. 
# 2), append the x(i,j) coordinates to the list b for row and c for column
# 3), set all the cell to 0 if they are in row i or column j

a = [[1, 2, 3],[0, 5, 6],[3, 8, 9],[10, 11, 0]]
b = []
c = []

for k in a:
    print k

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        if a[i][j] == 0:
            b.extend([i])
            c.extend([j])
print b, c

for i in range(0, len(b)):
    for j in range(0, len(a)):
        if b[i] == j:
            a[j] = [0]*(len(a[j]))
            
for i in range(0, len(c)):
    for j in range(0, len(a)):
        a[j][c[i]] = 0           

for k in a:
    print k
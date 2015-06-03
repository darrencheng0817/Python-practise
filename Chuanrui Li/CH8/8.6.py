#Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.


list1 = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
new_list1 = list1[0][1:3] + list1[1] + list1[2] + list1[3][1:3]              
print new_list1
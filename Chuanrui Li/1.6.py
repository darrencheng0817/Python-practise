# (1,2,3),(4
# (5,6,7,8
# 9,10,11,12),
# 13),(14,15,16)

# (4,8,12),(16
# (3,7,11,15
# 2,6,10,14),
# 1),(5,9,13)

# define seperated list to store the element during each rotation
# (1, 2, 3) -> first num of letter in list 1
# (5, 9, 13) -> starting number in the list 2, 3, 4
# (14, 15, 16) -> last num of letter in list 4
# (4, 8, 12) -> ending number in the list 1, 2, 3
# After each rotate, store everything in that level and clear the value in all the list. then start next iteration


# 1, delete the first and last rows
# 2, delete the most left and most right boundary in the rest of the rows
# 6,7
# 10,11  

# 7,11
# 6,10

# 6 -> 10
# 10 -> 11
# 11 -> 7
# 7 -> 6



def matrix():
    first = []
    second = []
    third = []
    forth = []
    a = [[0, 1, 2],[3, 4, 5], [6, 7, 8]]

#     a = [[0, 1, 2, 3, 4],[5, 6, 7, 8, 9], [10, 11, 12, 13, 14],[15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
    #the counter function
    row = 0
    column = 0
    counter = 0
    while (len(a[0])//2 > counter):
        for i in range(row, len(a)-row):
            for j in range(column, len(a[i])-column):
                #first num of letter in list 1
                if(i == row and j < len(a[i])-1-column):
                    first.append(a[i][j])
                #starting number in the list 2, 3, 4
                if(i != row and j == column):
                    second.append(a[i][j])
                #last num of letter in list 4
                if(i == len(a)-row-1 and j > column and j < len(a[i])-column):
                    third.append(a[i][j])
                # (4, 8, 12) -> ending number in the list 1, 2, 3
                if(i != len(a)-row-1 and j == len(a[i])-1-column):
                    forth.append(a[i][j])



        index1 = index3 = index4 = 0
        index2 = index4 = len(first) -1 - row
        for i in range(row, len(a)-row):
            for j in range(column, len(a[i])-column):
                if(i == row and j < len(a[i])-1-column):
                        a[i][j] = forth[index1]
                        index1 += 1
                if(i != row and j == column):
                        a[i][j] = first[index2]
                        index2 -=1
                if(i == len(a)-row-1 and j > column and j < len(a[i])-column):
                        a[i][j] = second[index3]
                        index3 += 1
                if(i != len(a)-row-1 and j == len(a[i])-1-column):
                        a[i][j] = third[index4]
                        index4 -=1


        first = []
        second = []
        third = []
        forth = []
        row += 1  
        column += 1
        counter += 1
    print first, second, third, forth
    print a
#     for i in a:
#         for j in i:
#             if(i == 1 &&):
#                 first.extend(j)
#                 print j
        
        
matrix()
            
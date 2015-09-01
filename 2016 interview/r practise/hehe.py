matrix = [
    [0,  0,    0,  -1,   0],
    [0, -1,    0,  'B',  0],
    [0, -1,   -1,  -1,   0], 
    [0, 'A',  -1,   0,   0], 
    [0,  0,   -1,   0,   0], 
    [0,  0,    0,   0,   0]
]

class Point:
    def __init__(x, y):
        self.x = x
        self.y = y

        
def is_valid(matrix, x, y):
    if x >= len(matrix) or y >= len(matrix[0]) or x < 0 or y < 0:
        return False
    else:
        return True
        

def bfs(matrix, a, b):
    # start at a
    # look for 0
    #
    list1 = []
    strx = a[0]
    stry = a[1]
    visited = set()
    list1.append(a)
    print list1
    while len(list1) != 0:
        print "---"
        print list1
        location = list1.pop()
        if location[0] == b[0] and location[1] == b[1]:
	       print matrix[location[0]][location[1]] 
	       return True
        if location not in visited:
            visited.add(location)
            if is_valid(matrix, location[0]+1, location[1]) and (matrix[location[0]+1][location[1]] == 0 or matrix[location[0]+1][location[1]] == 'B'):
    		    list1.append((location[0]+1,location[1]))
    			    #visited.add((location[0]+1,location[1]))
    			    
    	    if is_valid(matrix, location[0], location[1]+1) and (matrix[location[0]][location[1]+1] == 0 or matrix[location[0]][location[1]+1] == 'B'):
    		    list1.append((location[0],location[1]+1))
    			    #visited.add((location[0],location[1]+1))
    			    
    	    if is_valid(matrix, location[0]-1, location[1]) and (matrix[location[0]-1][location[1]] == 0 or matrix[location[0]-1][location[1]] == 'B'):
    		    list1.append((location[0]-1,location[1]))
    			    #visited.add((location[0]-1,location[1]))
    			    
    	    if is_valid(matrix, location[0], location[1]-1) and (matrix[location[0]][location[1]-1] == 0 or matrix[location[0]][location[1]-1] == 'B'):
    		    list1.append((location[0],location[1]-1))
    			    #visited.add((location[0],location[1]-1))
             
    return None
            
    
    
    
#bfs(matrix, Point(3, 1), Point(2, 4))
print bfs(matrix, (3, 1), (1, 3))




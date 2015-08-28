#Given a two dimensional graph with points on it, find a line which passes the most number of points.

#define a list of coordinates in one single list 
#do the brute force for every single points in the graph
#if the slope and the y-axis intersection is the same value
# ----- first time, define a new key and slope in the dictionary and add counter++
# ----- second time, increase the counter again
#in the end, find the highest counter, slope and value 


#define a list of coordinates in one single list 
list1 = [(1,1), (1,2), (2, 2), (2, 1), (3,3)]

#build up the data stuture for the map
storage = {}
def slope(cor1, cor2):
    # not a function return directly
    if cor2[0] - cor1[0] == 0:
        return 
    result = (cor2[1] - cor1[1]) / float(cor2[0] - cor1[0])
    #y = kx + b  => b = y - kx and also x = 0, b is intersection with y-axis
    b = cor1[1] - result*cor1[0]  
    return (result, b)
    

def calculate():
    global storage, list1
    #do the brute force for every single points in the graph
    for i in range(0, len(list1)):
        print "This is "+ str(list1[i]) + "\n"
        for j in range(i+1, len(list1)):
            print list1[i], list1[j]
            key = slope(list1[i], list1[j])
            if key != None:
                if key not in storage:
                    storage[key] = 1
                else:
                    storage[key] += 1
    #the trick to print in one ine
    #print storage
    
    #checking the ans
    ans = 0
    max_counter = 0
    for key in storage:
        if storage[key] > max_counter:
            max_counter = storage[key]
            ans = key
    print "This is the answer: " + "k = " + str(ans[0]) + ", b = " + str(ans[1])

calculate()
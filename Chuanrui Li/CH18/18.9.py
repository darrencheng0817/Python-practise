#Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.



#for the program, if we only need to insert one element in either maxheap or minheap, this only takes about O(log(n)) to maintain

import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!

listMin = []
listMax = []

for i in listForTree:
    if len(listMin) == len(listMax):
        listMax = listMax + [i]
        heapq._heapify_max(listMax) 
    else:
        listMin = listMin + [i]
        heapq.heapify(listMin) 
    
#Find the min
if len(listMin) != len(listMax):
    print listMax[0]
else:
    print listMin[-1]
        


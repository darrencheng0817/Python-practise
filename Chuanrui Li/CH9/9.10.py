#You have a stack of n boxes, with widths wi, heights hi, and depths di. The boxes cannot be rotated
#and can only be stacked on top of one another if each box in the stack is strickly larger than the box 
#above it in width, height, and depth.

#Implement a method to build the tallest stack possible, where the height of a stack is 
#the sum of the heights of each box


#the example we can have: b1 > b2 > b3 > b4 (based on width, height, and depth)
#Input b3 b1 b2 b4
#Output b1 b2 b3 b4 (from bottom to top)

#There is four options for these recursion tree -> first level can be solved by a for loop
#retirction checking during each time the recursion stack updating
#global list to store the max height result

#input list and temperary stack for the result for the recuersive function
from copy import deepcopy
result = []
max_length = 4

  


def update(list1, temp):
  global result
  global max_length

  if len(temp) >= max_length+1:
    #print "hehe"
    #print temp
    #this base is not useful, it is the last step, will not save any extra steps for checking
    return
  else:
    for i in list1:
        #updating temp
        update(list1, temp + [i])
        #print temp
       
        if len(temp) >= len(result):
          
          j = 0
          increment = True
          while j+1 < len(temp):
            if temp[j+1] <= temp[j]:
              increment = False
            j += 1
          if increment == True:
            #print "haha"
            #updating final result
            result = deepcopy(temp)
       
        


def main():
  #assuming 1 is the biggest, 4 is the smallest
  global result
  temp = []
  list1 = [2, 1, 4, 3]
  update(list1, temp)
  print "------------------"
  print result
  

if __name__ == "__main__":
    main()













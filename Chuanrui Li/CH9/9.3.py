#A magic index in an array A[1..n-1] is defined to be an index such that A[i] = i.
#Given a sorted array of distinct integers, write a method to find a magic index, if one exist, in array A.

#Follow up, what if the value is not distinct


#1), example below, using a sorted array of distinct integers condition:
# - index ------ 0, 1, 2, 3, 4, 5, 6 
# - data ------- 1, 2, 5, -, -, -, 6
# we can skip some comparisons

def magic_number(list1):
  for i in range(0, len(list1)):
    #when index < data
    if list1[i] > i:
      return None
    else:
      if list1[i] == i:
        return list1[i]
      

def magic_number1(list1):
  i = 0
  while i < len(list1):
    #when index < data
    if list1[i] > i:
      i = list1[i]
      #check length of the array
      if i > len(list1):
        return None
    else:
      if list1[i] == i:
        return list1[i]
      i += 1
      
#I missed the negative value cases and binary search is much better
def magic_number2(list3, start, end):
  #checking out out of bound or cannot find a result in the list
  if start < 0 or end >= len(list3) or start > end:
    return -1
  mid = (start + end) / 2
  print mid, start, end, list3[mid]
  if mid == list3[mid]:
    return mid
  #index > data:
    #right ->
  #index < data
    #left <-
  elif mid < list3[mid]:
    return magic_number2(list3, start, mid-1)
  elif mid > list3[mid]:
    return magic_number2(list3, mid+1, end)
  
  
        

def main():
  #a sorted array of distinct integers condition
  list1 = [2, 2, 2, 6]
  #print magic_number(list1)
  
  #a sorted array of non - distinct integers condition
  list2 = [3, 3, 3, 3]
  #print magic_number1(list2)  
  
  #a sorted array of distinct integers
  list3 = [-10, -1, 0, 2, 3]
  #0, 1, 2, 3, 4 -> mid = 2
  print magic_number2(list3, 0, len(list3)-1)  
  
  #a sorted array of distinct integers
  list4 = [-10, -1, 0, 2, 3]  
  
  
  
  

  
    

if __name__ == "__main__":
    main()













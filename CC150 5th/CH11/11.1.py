#You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. 
#Write a method to merge B into A in sorted order.
        
#A = [1, 2, 3, 5, 6]
#B = [0, 1, 2, 3, 4]

#since there are two sorted arrays, the first one in both list is always the smallest one
#1), compare the smallest one in both list, pop the smallest and insert into a new list
#2), repeat, until both lists are empty.



def main():
  list1 = [1, 2, 3, 5, 6]
  list2 = [0, 1, 4]
  result = []
  #this is the starting value
  i = 0
  j = 0
  while i < len(list1) and j < len(list2):
  	if list1[i] > list2[j]:
  		result = result + [list2[j]]
  		j += 1
  	else:
  		result = result + [list1[i]]
  		i += 1

  #adding the rest of data
  if i < len(list1):
  	result = result + list1[i:]

  if j < len(list2):
  	result = result + list2[j:]

  print result

 
if __name__ == "__main__":
    main()













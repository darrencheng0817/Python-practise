#A circus is designing a tower routine consisting of people standing atop one anoth- er’s shoulders. 
#For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. 
#Given the heights and weights of each person in the circus, write a method to compute the largest possible number of peo- ple in such a tower.



#EXAMPLE:
#Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
#Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)





# 1,) real problem -> sort a pair of data in the increasing order
# 2,) using insertion sort


def swap(j, i, list1):
	temp = [(0,0)]
	temp = list1[j]
	list1[j] = list1[i]
	list1[i] = temp




def sort_pair(list1):
	i = 0
	while i < len(list1):
		j = 0
		while j < i:
			#print "hehe"
			if list1[j][0] > list1[i][0] and list1[j][1] > list1[i][1]:
				#print "$$$$$$$$$$$$$$$$"
				#print list1[j][0], list1[j][1], list1[i][0], list1[i][1]
				swap(j, i, list1)
				i -= 1
				break
			j += 1
		i += 1




def main():
	list1 = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
	list2 = [(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)]
	sort_pair(list1)
	print list1
  

if __name__ == "__main__":
	main()
 


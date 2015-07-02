#Given an array of integers, write a method to find indices m and n such that if you 
#sorted elements m through n, the entire array would be sorted. Minemize n - m (that is, find the 
#smallest such sequence)

#ex: 1, 2, 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19

#1), step1: read from both sides of the list and stop when the list is not sorted
#---> result: [1, 2, 4, 7, 10, 11] & [8, 12] & [5, 6, 16, 18, 19]
#2), step2: satisfy two conditions: 
#---> left[biggest] < mid[smallest] && mid[biggest] < right[smallest]

#result --> [1, 2, 4, 7]   [10, 11] & [8, 12] & [5, 6]    [16, 18, 19]

def findMin(list1):
	#forward
	midS = 0
	midE = 0
	listF = []
	i = 0
	while i < len(list1)-2:
		if list1[i] < list1[i+1]:
			listF += [list1[i]]
		else:
			midS = i
			break
		i += 1
	#extra value
	if i != len(list1):
		if list1[i-1] < list1[i]:
			listF += [list1[i]]
	#backward
	listB = []
	j = len(list1)-1
	while j > 1:
		if list1[j-1] < list1[j]:
			listB = [list1[j]] + listB
		else:
			midE = j
			break
		j -= 1
	
	#extra value
	if j != -1:
		if list1[j] < list1[j+1]:
			#print "hehe"
			listB = [list1[j]] + listB
			
	
	#mid list
	listMid = list1[midS+1: midE]
	Bmax = max(listMid)
	Bmin = min(listMid)
	#print "hehehe"
	for k in range(0, len(listF)):
		#print "xixixi"
		if listF[k] > Bmin:
			midS = k
			break

	for k in range(0, len(listB)):
		#print "jijiji"
		#print k
		if listB[k] >= Bmax:
			midE += k
			break
	print "final answer is:"
	print midE -midS

def main():
	list1 = [1, 2, 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19]
	findMin(list1)
  

if __name__ == "__main__":
	main()


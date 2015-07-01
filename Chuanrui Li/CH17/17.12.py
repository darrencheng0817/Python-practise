#Design an algorithm to find all pairs of integers within an array which sum to a specified value.



table = {}
result = []
def hashMethod(list1, value):
	global result
	
	#set up the hash map first
	for index in range(0, len(list1)):
		if list1[index] not in table:
			table[list1[index]] = index


	
	#check the list2
	for index in range(0, len(list1)):
		checker = value - list1[index]
		if checker in table:
			if table[checker] > index:
				result = result + [(list1[index], checker)]

result1 = []

def bSearch(list1, lookValue, Currindex, start, end):
	global result1
	#print start,end
	if start > end:
		#print "hehe"
		return
	mid = (start + end)/2
	if list1[mid] == lookValue and Currindex < mid:
		result1 = result1 + [(lookValue, list1[Currindex])]
	elif list1[mid] > lookValue:
		#print "hehe1"
		end = mid - 1
		bSearch(list1, lookValue, Currindex, start, end)
	elif list1[mid] < lookValue:
		#print "hehe2"
		start = mid + 1
		bSearch(list1, lookValue, Currindex, start, end)

def binaryMethod(list1, value):
	for i in range(0, len(list1)):
		lookValue = value - list1[i]
		#print lookValue, i
		bSearch(list1, lookValue, i, 0, len(list1))
	
	print result1
	
def main():
	#I assume there is no duplicates in the array
	list1 = [1, 2, 3, -1, 4, -2]
	value = 2
	hashMethod(list1, value)
	
	list1.sort()
	binaryMethod(list1, value)
	
	
if __name__ == "__main__":
	main()


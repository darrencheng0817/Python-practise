#You are given an array of integers (both positive and negative). 
#Find the continuous sequence with the largest sum. Return the sum.

# EXAMPLE
# Input: {2, -8, 3, -2, 4, -10}
# Output: 5 (i.e., {3, -2, 4} )

#1), an outer for loop -> iterate every num in the list, can compare with the max current result
#2), an inner for loop -> to increment the selected list size, if the result does not go negative

def findMax(list1):
	index = 0
	#this used for tracking the biggest result
	maxValue = 0
	while index < len(list1):
		if list1[index] > 0:
			#This is the inner loop
			sumV = 0
			result = 0
			index2 = index
			while index2 < len(list1):
				sumV += list1[index2]
				if sumV < 0:
					break
				else:
					result = sumV
				index2 +=1
			#Then updating the value
			if result > maxValue:
				maxValue = result

		index += 1
	print maxValue

def main():
	list1 = [2, -8, 3, -2, 4, -10, 4, 4]
	findMax(list1)
  

if __name__ == "__main__":
	main()


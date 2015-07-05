#Write a program to find the longest word made of other words in a list of words.

# Input: test, tester, testertest, testing, testingtester 
# Output: testingtester

def main():
	hashmap = {}
	list1 = ["test", "tester", "testertest", "testing", "testingtester"]
	list1.sort()
	list1.reverse()
	print list1
	for i in list1:
		if i not in hashmap:
			hashmap[i] = 1
	
	#check the longest word
	for element in list1:
		#inner loop to check each element
		
		outer = 0
		start = 0
		final = []
		while outer < len(element):
			index = outer
			temp = []
			while index <= len(element):
				if element[start:index] in hashmap and element[start:index] != element:
					temp = temp + [element[start:index]]
					index += 1
					#print "------------"
					#print element
					#print temp, outer, index
				index += 1
			if len(temp) == 0:
				outer += 1
			else:
				tempResult = max(temp)
				final = final + [tempResult]
				increment = len(tempResult)
				outer += increment
				start = outer
		#final cheaking, break the list earlier
		if ''.join(final) == element:
			print element
			break
		
		
if __name__ == "__main__":
	main()


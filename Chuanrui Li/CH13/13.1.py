#Write a method to print the last K lines of an input file using C++.
#It is similar to write into the python
#The logic is similar to the page eviction -> most recent used the k lines

def main():
	#tracking the least recent used number
	tracking = 0
	k = 3
	counter = 0
	list1 = []
	file = open("sample.txt")
	index = 0
	while 1:
		line = file.readline().splitlines()	
		if not line:
			break
		if index < k:
   			list1 = list1 +[line]
   			index += 1
   		else:
   			list1[tracking] = line
   			tracking += 1
   			if tracking >= k:
   				tracking = 0	

 	print list1




if __name__ == "__main__":
	main()




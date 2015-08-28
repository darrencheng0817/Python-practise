#Write a method to randomly generate a set of m integers from an array of size n. 
#Each element must have equal probability of being chosen.

import random

def main():
	array = [1, 2, 3, 4, 5, 6, 7, 8]
	newarray = []
	limit = 4
	
	for index in range(0, len(array)):
		Nindex = random.randrange(0, index+1)
		if len(newarray) <= 4:
			newarray = newarray + [array[Nindex]]
		elif Nindex < limit:
			newarray[Nindex] = array[index]
	print newarray
		
if __name__ == "__main__":
	main()




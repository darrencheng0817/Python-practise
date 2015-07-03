#Write a method to shuffle a deck of cards. 
#It must be a perfect shuffle - in other words, each 52! permutations of the deck has to be equally likely. 
#Assume that you are given a random number generator which is perfect.


#solution: first we need to make sure n-1 is shuffled, then we swap the nth element with one of the n-1 elements
#We can solve this by iteration

import random

def main():
	array = [1, 2, 3, 4, 5]
	for index in range(0, len(array)):
		Nindex = random.randrange(0, index+1)
		temp = array[Nindex]
		array[Nindex] = array[index]
		array[index] = temp
	print array	
  

if __name__ == "__main__":
	main()




#imagine you are reading in a stream of integers. Periodically, yo wish to be able to look up 
#the rank of a number x (the number of values less than or equal to x). Implement the data structure
#algorithm to support these operations. That is, implement the method track(int x), which is called when
#each number is generated, and the method getRankofNumber(int x), which returns the number of values
#less than or equal to x (Not include x itself)

#Example:
#stream(in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
#1, 3, 4, 4, 5, 5, 7, 9, 13
#5, 1, 4, 4, 5, 9, 7, 13, 3

# getRankofNumber(1) = 0
# getRankofNumber(3) = 1
# getRankofNumber(4) = 3 => 1, 2, 4 (cos there are two 4s)

#1), using the hash table to store the integers as a hash key and store the counter as rank
#2), add a flag for the duplicated key => solving #less than or equal to x (Not include x itself)

def track(i, hash_map):
	if i not in hash_map:
		hash_map[i] = [0, False]
		#find the max less than i
		maxk = -1
		for k in hash_map:
			if k < i:
				if maxk < k:
					maxk = k
		if maxk != -1:
			hash_map[i][0] = hash_map[maxk][0] + 1		
	else:
		hash_map[i][0] = hash_map[i][0] + 1
		hash_map[i][1] = True	
	#increment the ranking for other keys
	for k in hash_map:
		if k > i:
			hash_map[k][0] = hash_map[k][0] + 1




def getRankofNumber(x):
	pass

def main():
	hash_map = {}
	stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]
  	for i in stream:
  		track(i, hash_map)
  	print hash_map
  

if __name__ == "__main__":
	main()




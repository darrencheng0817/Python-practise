#Design a method to find the frequency of occurrences of any given word in a book.

#Solution: Single Query -> best can do O(n)


#Solution: Repetitive Queries -> hashmap -> best can do O(n) 

book =["I", "am", "a", "book" "..."]

hashmap = {}
def setup():
	for i in book:
		if i in hashmap:
			hashmap[i] += 1
		else:
			hashmap[i] = 1



def main():
	#set up words
	setup()
	w = "hehe"

	if len(book) == 0:
		print "No words in book"
	else:
		if w in hashmap:
			print hashmap[w]
		else:
			print "no find"

	findMin(list1)
  

if __name__ == "__main__":
	main()


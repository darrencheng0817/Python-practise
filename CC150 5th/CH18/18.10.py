#Given two words of equal length that are in a dictionary,write a method to transform one word into another word by changing only one letter at a time. The new word you get in each step must be in the dictionary.
#EXAMPLE:
#Input: DAMP, LIKE
#Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE

#solution: BFS
class Queue:
	def __init__(self, item):
		self.items = [item]

	def dequeue(self):
		return self.items.pop()

	def enqueue(self, item):
		return self.items.insert(0,item)

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

def main():
	dictionary = ["DAMP", "LAMP", "LIMP", "LIME", "LIKE"]
	start = "DAMP"
	required = "LIKE"
	Queue1 = Queue(start)
	#mark the traveled value
	list1 = []
	while len(Queue1.items) != 0:
		input1 = Queue1.peek()
		for i in range(0, len(input1)):
			s = list(input1)
		   	r = list(required)
		   	s[i] = r[i]
		   	news = "".join(s)
	   		if news in dictionary and news not in list1 and news != input1:
	   			Queue1.enqueue(news)

	   	list1 = list1 + [Queue1.dequeue()]
	print list1

		
if __name__ == "__main__":
	main()
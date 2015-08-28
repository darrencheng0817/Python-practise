#Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7.
#This is the dynamic programming problem, we need to find the recursive relation first
#------ base case: n = 3, k = 1th number
#------ upper case: n(k) = min(q1, q2, q3) k > 1 ----- q1, q2, q3 are 
#------ 3*A1, 3*A2, 3*A3

#implementation plan
#maintain three prority queue using list to keep track of three smallest value
#Q1 == q1 * A1, Q2 == q2 * A2, Q3 == q3 * A3 


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

def find_prime():
	prime_th = 12
	smallest = 0
	list_3 = Queue(3)
	list_5 = Queue(5)
	list_7 = Queue(7)
	while prime_th > 0:
		#find the min
		smallest = min(list_3.peek(), list_5.peek(), list_7.peek()) 
		#do the insertion to prevent the duplicates 3*7, 7*3
		# the priority is list_7, list_5, list_3
		if smallest == list_3.peek():
			list_3.dequeue()
			list_3.enqueue(3*smallest)
			list_5.enqueue(5*smallest)
			list_7.enqueue(7*smallest)
		elif smallest == list_5.peek():
			list_5.dequeue()
			list_5.enqueue(5*smallest)
			list_7.enqueue(7*smallest)
		elif smallest == list_7.peek():
			list_7.dequeue()
			list_7.enqueue(7*smallest)
		#enqueue this level 
		
		

		prime_th -= 1
	print list_3.items, list_5.items, list_7.items
	print smallest






find_prime()

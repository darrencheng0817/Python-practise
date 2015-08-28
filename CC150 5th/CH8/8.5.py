#Design the data structures for an online book reader system
#» User membership creation and extension.
#» Searching the database of books
#» Reading the books


class library:
	def __init__ (self):
		self.book = {1: "hehe", 2: "haha", 3: "xixi"}

class reader(library):
	#this is an inheritance from the base define function
	def __init__ (self, ID, days_left):
		library.__init__(self)
		self.ID = ID
		self.data = days_left

	def extension(self, days_left):
		self.data = days_left
	
	def search(self, BID):
		for i in self.book:
			if BID == i:
				print self.book[i]
		
				


r1 = reader(1, 30)
r2 = reader(2, 21)


r1.search(5)

  		  
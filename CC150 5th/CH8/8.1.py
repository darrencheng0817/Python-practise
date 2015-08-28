#Design the data structures for a generic deck of cards. 
#Explain how you would sub- class it to implement particular card games

#some of my assumption for the blackjack
#--- each guy picks up four cards, at the end, the value of each card need to be summed up
#--- also, if the sum is greater than 21, the guy dies 

#-- hold a card information
class cards:
	def __init__(self, points, card_type):
		self.points = points
		self.type = card_type

	def get_points(self):
		return self.points

	def get_type(self):
		return self.type

#-- hold the player information
class player:
	def __init__(self, name):
		self.name = name
		self.__sum = 0
		self.__counter = 0

	def get_card(self, cards):
		self.__sum += cards.get_points()
		self.__counter += 1
		if self.__counter == 4:
			print "Game ends, here is your marks: " +  str(self.__sum)
			if self.__sum > 21:
				print "die"

	def current_sum(self):
		print self.__sum, self.__counter
		

#Real game plan starts here
player1 = player("hehe")
player2 = player("haha")
CA = cards(11, "1")
C2 = cards(2, "1")
C3 = cards(3, "1")
C4 = cards(4, "2")
C5 = cards(5, "3")
C6 = cards(6, "2")
C7 = cards(7, "3")


#pick up the cards
player1.get_card(C6)
player1.get_card(C6)
player1.get_card(C6)
player1.get_card(C6)

player2.get_card(C4)
player2.get_card(C4)
player2.get_card(C5)
player2.get_card(C4)











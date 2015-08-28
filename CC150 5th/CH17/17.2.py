#Design an algorithm to figure out if someone has won in a game of tic-tac-toe. 
#Normally for tic-tac-toe, we have a 3*3 board


#easy approach: check 8 lines, 3 vertical, 3 horizontal, 2 daigonal 

#hard approach: 
#1), using the hash map to preload all the info -> all the cases -> who wins
#2), then calculate the map value and then try to match the hash code

def main():
	#"empty" is 0, "o" is 1, "x" is 2. ----> 
	# 111
	# 111000
	# 111000000

	# 222
	# 222000
	# 222000000

	# 100010001
	# 001010100

	# 200020002
	# 002020200

	hash_map = {111: "o wins", 111000: "o wins", 111000000: "o wins", 100010001: "o wins", 1010100: "o wins", 222: "x wins", 222000: "x wins", 222000000: "x wins", 200020002: "x wins", 2020200: "x wins"}

	key = 0
	factor = 0
	board = [1,0,0,0,1,0,0,0,1]

	#reverse counting
	for i in range(0, len(board)):
		key += board[i]*pow(10, factor)
		factor += 1

	print key
	if key in hash_map:
		print hash_map[key]
	else:
		print "no result"
  

if __name__ == "__main__":
	main()




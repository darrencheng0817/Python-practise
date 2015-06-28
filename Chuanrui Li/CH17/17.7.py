#Write an algorithm which computes the number of trailing zeros in n factorial.

#check how many (5 and 2) pairs in the number
#--> counting the number of 5s in the final number
def trailing_zeros(N_input):
	i = 5
	counter = 0
	while i <= N_input:
		#print i
		#check the # is power of 5
		inner_counter = 0
		new_num = i / 5
		while new_num % 5 == 0 and new_num != 0:
			#print "hehe"
			counter +=1
			new_num = new_num / 5
		
		counter += 1
		i += 5
	print counter

def main():
	N_input = 5
	trailing_zeros(N_input)
	

if __name__ == "__main__":
	main()




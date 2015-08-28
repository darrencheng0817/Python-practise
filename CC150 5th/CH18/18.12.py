
#Given an NxN matrix of positive and negative integers, 
#write code to find the submatrix with the largest possible sum.
matrix = [[1, 1, 0],[0, 1, 0],[0, 0, 0]]

def sum1(Xinner, Yinner):
	#print Yinner, Xinner
	return matrix[Yinner][Xinner]

def sum2(YinnerS, YinnerE, XinnerS, XinnerE):
	init = XinnerS
	sumV = 0
	while YinnerS <= YinnerE:
		XinnerS =init
		while XinnerS <= XinnerE:
			#print YinnerS, XinnerS
			# vertical, then horizontal
			sumV += matrix[YinnerS][XinnerS]
			#print sumV
			XinnerS += 1
		YinnerS += 1
	return sumV

	
	
	
def main():
	global matrix
	sumV = float("-inf")
	x = []
	y = []
	Yinner = 0
	while Yinner < len(matrix):
		Xinner = 0
		while Xinner < len(matrix): 
			result = sum1(Xinner, Yinner)
			if result > sumV:
				print "haha"
				sumV = result
				x= []
				y= []				
				x += [Xinner]
				y += [Yinner]
			Xinner += 1
		Yinner += 1
	
	
	length = 1
	while length < len(matrix):
		Yinner = length			
		while Yinner < len(matrix):
			Xinner = 0
			while Xinner < len(matrix): 
				diff = 0
				while diff <= length:
					
					#print (Yinner,Xinner)
					
					#(0, 2, 0, 2) --> extreme case and check at the end
					if Yinner-length == 0 and Xinner-diff == 0 and Yinner == length and Xinner == length:					
						break
					#cover all the cases, but skip the negative value
					if Xinner - diff >= 0:
						#print (Yinner-length, Yinner, Xinner-diff, Xinner)
						#(0, 2, 1, 2)
						result = sum2(Yinner-length, Yinner, Xinner-diff, Xinner)
						if result > sumV:
							#print length
							#print "hehe"
							sumV = result
							x= []
							y= []
							x += [Xinner-diff, Xinner]
							y += [Yinner-length, Yinner]
				
						#(1, 2, 0, 2)
						#print (Xinner-diff, Xinner, Yinner-length, Yinner)
						result = sum2(Xinner-diff, Xinner, Yinner-length, Yinner)	
						if result > sumV:
							print "hihi"
							sumV = result
							x= []
							y= []
							x += [Yinner-length, Yinner]
							y += [Xinner-diff, Xinner]						
					diff += 1
				Xinner += 1
			Yinner += 1
		length += 1		
	print "-----------hehe"	
	
	#2 and more Units, square ---> this part is redundant
	length = 1
	while length < len(matrix):
		Yinner = length			
		while Yinner < len(matrix):
			Xinner = length
			while Xinner < len(matrix): 
				#print (Xinner-length, Xinner, Yinner-length, Yinner)
				#print (Xinner-1, Xinner, Yinner)
				#print (Yinner,Xinner)
				result = sum2(Yinner-length, Yinner, Xinner-length, Xinner)
				#print result
				if result > sumV:
					print "xiha"
					#print (Xinner-length, Xinner, Yinner-length, Yinner)
					sumV = result
					x= []
					y= []
					x += [Xinner-length, Xinner]
					y += [Yinner-length, Yinner]
				Xinner += 1
			Yinner += 1
		length += 1
		
	
	
		
	print "final result ----"
	print 	sumV, x, y

		
if __name__ == "__main__":
	main()
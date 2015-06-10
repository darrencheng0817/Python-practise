# Given a boolean expression consisting of the symbols 0, 1, &, |, and ^, and a desired boolean 
# result value result, implement a function to count the number of ways of parenthesizing the expression
# such that it evaluates to result

#example:
#input: f(1^0|0|1, true)
#output: the number of ways 

#method, 1^0|0|1 => 1^(0|0|1), (1^0)|(0|1), (1^0|0)|1

def ans(start, end, operations, result):
	if start >= end-1:
		
		print "hehe"
		if operations[start] == '1' and result == True:
			return 1
		if operations[start] == '0' and result == False:
			return 1
			#this is same logic
		return 0

	if result == True:
		i = start
		while i < end:
			#find the value for each operation
			if operations[i] == '^':
				return ans(start, i-1, operations, True) * ans(i+1, end, operations, False) + ans(start, i-1, operations, False) * ans(i+1, end, operations, True)
			elif operations[i] == '&':
				return ans(start, i-1, operations, True) * ans(i+1, end, operations, True)
			elif operations[i] == '|':
				return ans(start, i-1, operations, True) * ans(i+1, end, operations, True) + ans(start, i-1, operations, True) * ans(i+1, end, operations, False) + ans(start, i-1, operations, False) * ans(i+1, end, operations, True)
			i += 1		
	if result == False:
		#this is same logic, different true, false conditions
		i = start
		while i < end:
			#find the value for each operation
			if operations[i] == '^':
				return ans(start, i-1, operations, True) * ans(i+1, end, operations, True) + ans(start, i-1, operations, False) * ans(i+1, end, operations, False)
			elif operations[i] == '&':
				return ans(start, i-1, operations, False) * ans(i+1, end, operations, False) + ans(start, i-1, operations, True) * ans(i+1, end, operations, False) + ans(start, i-1, operations, False) * ans(i+1, end, operations, True)
			elif operations[i] == '|':
				return ans(start, i-1, operations, False) * ans(i+1, end, operations, False)
			i += 1


def main():
	operations = ['1', '|', '1', '|', '1']
	result = True
	print ans(0, len(operations), operations, result)
  

if __name__ == "__main__":
	main()




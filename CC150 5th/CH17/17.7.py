#Given an integer between 0 and 999,999, 
#print an English phrase that describes the integer (eg, “One Thousand, Two Hundred and Thirty Four”).

# EX: 999,999 --->
# nine hundred ninety-nine thousand, 
# nine hundred ninety-nine 
#1), break down the words and do it into different cases -> for 999,000 it just a

def words(num, position, list1):
	#This is for the first position 
	result = 0
	if (position == 1 and list1[len(list1)-2] != 1) or position == 3:
		if num == 1:
			result = "one"
		elif num == 2:
			result = "two"
		elif num == 3:
			result = "three"
		elif num == 4:
			result = "four"
		elif num == 5:
			result = "five"
		elif num == 6:
			result = "six"
		elif num == 7:
			result = "seven"
		elif num == 8:
			result = "eight"
		elif num == 9:
			result = "nine"
		else:
			result = "none"
		#This is for the third position 
		if position == 3:
			result += " hundred and "
		return result

	#This is for the second position 		
	if position == 2:
		if num == 1:
			if list1[-1] == 0:
				result = "ten"
			elif list1[-1] == 1:
				result = "Eleven"
			elif list1[-1] == 2:
				result = "Twelve"
			elif list1[-1] == 3:
				result = "Thirteen"
			elif list1[-1] == 4:
				result = "Fourteen"
			elif list1[-1] == 5:
				result = "Fifteen"
			elif list1[-1] == 6:
				result = "Sixteen"
			elif list1[-1] == 7:
				result = "Seventeen"
			elif list1[-1] == 8:
				result = "Eighty"
			elif list1[-1] == 9:
				result = "Nineteen"			
			
		elif num == 2:
			result = "Twenty"
		elif num == 3:
			result = "Thirty"
		elif num == 4:
			result = "Forty"
		elif num == 5:
			result = "Fifty"
		elif num == 6:
			result = "Sixty"
		elif num == 7:
			result = "Seventy"
		elif num == 8:
			result = "Eighty"
		elif num == 9:
			result = "Ninety"
		else:
			result = "none"
		#have a digit on "0" position
		if list1[-1] != 0 and num != 1 and num != 0:
			result += "-"
		return result



def parser(list1):
	print list1
	result = ""
	position = len(list1)
	for i in list1:
		hehe = words(i, position, list1)
		if hehe != "none":
			result += hehe
		position -= 1
	print result  


def main():
	#Input is only three digits
	num = 888
	list1 = [int(i) for i in str(num)]
	parser(list1)
	

if __name__ == "__main__":
	main()




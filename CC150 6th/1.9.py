#Rotate string
#'waterbottle' & 'erbottlewat', must use the substring checking method
#-> True, this is a rotated substring

str1 = 'waterbottle'
str2 = 'erbottlewat'

def substring(str1, str2):
	if str2 in str1:
		return True
	else:
		return False


def stringR():
	global str1, str2
	str1 = str1 + str1
	print substring(str1, str2)

stringR()
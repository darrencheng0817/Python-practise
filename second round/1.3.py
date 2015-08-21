#URLify
#Example:
#'Mr John Smith    ', 13
#-> "Mr%20John%20Smith"

#in the URL, the assume %20 is only in the middle of the string
#iteration the list -> size seems redundant


str1 = 'Mr John Smith    '
size = 20
list1 = []

def url():
	global str1, list1

	length = len(str1)
	for i in range(0,length-1):
		if str1[i] == ' ' and str1[i+1] == ' ':
			break
		elif str1[i] == ' ' and str1[i+1] != ' ':
			list1 = list1 + ['%20']
		else:
			list1 = list1 + [str1[i]]

	str1 = ''.join(list1)

url()
print str1
		
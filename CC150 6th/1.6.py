#String compression
# 'aabcccccaaa'
#-> 'a2b1c5a3'
#Compress the string

str1 = 'aabcccccaaa'

def compress():
	global str1
	list1 = []
	#checking the number, letter
	counter = 1
	first = ''
	for i in range(0, len(str1)-1):	
		first = str1[i]	
		if str1[i] == str1[i+1]:
			counter += 1
		else:
			list1 += [first + str(counter)]
			counter = 1
			first = ''
	list1 += [str1[-1] + str(counter)]
	print list1
	str2 = ''.join(list1)
	if len(str1) < len(str2):
		print str1
	else:
		print str2

compress()
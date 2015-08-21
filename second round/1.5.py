#One array
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false

#1, the one break into two
#2, case1 
		# iterate all the letters and only has one miss
#3, case2
		# iterate all the letters and only has one add
#4, case3
		# iterate all the letters and only has one diff

str1 = "pale, paal"
list1 = []

def check():
	global str1, list1
	list2 = []
	#not used, just demo
	list3 = []
	#one step solution
	list3 = [x.strip() for x in str1.split(',')]
	
	list1 = str1.split(',')

	for i in list1:
		list2 += [i.strip()]
		
	print list2
	
	#length
	if len(list2[0]) != len(list2[1]) and len(list2[0]) != (len(list2[1]) + 1) and len(list2[0]) != (len(list2[1]) - 1):
		print "die"
		return False
	elif len(list2[0]) == (len(list2[1]) + 1):
		print "haha"
		#case1, missing 
		counter = 0
		i = j = 0
		while j < len(list2[1]):
			if list2[0][i] == list2[1][j]:
				i+= 1
				j+= 1
			else:
				counter += 1
				i+= 1
				if counter == 2:
					print "die"
					return False
		print "win"
		return True
	elif len(list2[0]) == (len(list2[1]) - 1):
		print "xixi"	
		#case1, missing 
		counter = 0
		i = j = 0
		while j < len(list2[0]):
			if list2[1][i] == list2[0][j]:
				i+= 1
				j+= 1
			else:
				counter += 1
				i+= 1
				if counter == 2:
					print "die"
					return False
		print "win"
		return True
	elif len(list2[0]) == len(list2[1]):
		print "lele"	
		#case1, missing 
		counter = 0
		i = j = 0
		while j < len(list2[0]):
			if list2[1][i] != list2[0][j]:
				counter += 1
				if counter == 2:
					print "die"
					return False
			i+= 1
			j+= 1
		print "win"
		return True
	else:
		print "die"
		return False



check()



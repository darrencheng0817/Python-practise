#Palidrome Permutation
#"Tact Coa"
#-> True (permutation: "taco cat", "atco cta")

#1, space does not matter
#2, repeat letters, only one can be not repeated
#3, the low or capital cases does not matter


str1 = "Tactc Cca"
hashtable = {}


def checking():
	global str1, hashtable
	str1 = str1.lower()
	for i in str1:
		if i == ' ':
			pass
		elif i not in hashtable:
			hashtable[i] = 1
		else:
			hashtable[i] += 1
			
	#checking the result
	counter = 0
	for key in hashtable:
		if hashtable[key] % 2 != 0:
			counter += 1
		if counter > 1:
			print "false"
			return
	print "True"



		

checking()



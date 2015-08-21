#In premutation the order does matter
#'abc', 'bac' -> yes
a = 'abbc'
b = 'baac'

def checking():
	global a, b
	a = ''.join(sorted(a))
	b = ''.join(sorted(b))
	
	if a == b:
		print "yes"
	else:
		print 'No'


checking()

def say_hello():
    print 'Hello, World'

def reverse1():
    a = "abaca"
    for outer in range(0, len(a)):
        print a[-(outer+1)]
        
def reverse2():
    a = "abaca"
    for outer in range(0, len(a)):
        print a[len(a)-(outer+1)]
        
def reverse3():
    a = "abaca"
    print a[::-1]

def reverse4():
    a = "abaca"
    a = ''.join(reversed(a))
    print a

#swapping character
def reverse3():
	a = "abacd"
	a = list(a)
	for i in range(0, len(a)-1):
		print i, len(a)-i
		if(i >= len(a)-1-i):
			break
		else:
			temp = a[i]
			a[i] = a[len(a)-i-1]
			a[len(a)-i-1] = temp
	print ''.join(a)

reverse3()
reverse4()
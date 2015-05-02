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

reverse4()
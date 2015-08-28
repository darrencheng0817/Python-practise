def true_length():
    a = "hi, I am Richard   "
    size = 5
    if(len(a)<size):
        add = len(a)-size
        a = a.replace(" ", "%20")
        for i in range(0, add):
            a += "%20"
        print a
    elif len(a)>size:
        a = a[0:size]
        a = a.replace(" ", "%20")
        print a
            
def string_compression():
    flag = 1
    s = "aaafd"
    a = []
    counter = 1
    index = 1
    first = 0
    flag1 = 1
    
    
    
    while (counter < len(s)):
        first = 0
        
        print "result"
        if first == 0:
            a.extend([s[counter], 1])
        while s[counter-1] == s[counter]:
                first = 1
                flag1 = 0
                if first == 1:
                    a[index] = a[index] + 1
                    counter = counter + 1
                if(counter == len(s)):
                    break         
        if first == 0:
            counter = counter + 1
        index = index + 2
    print a 
    
    for i in range(0, len(a)):
        if len(a) == i+2:
                break
        if a[i] == a[i+2] and a[i+1] == 1:
           a[i] = " "
           a[i+1] = " "
            
            
    while True:
        if ' ' in a:
             a.remove(' ')
        else:
            break
    
    if flag1 == 1:
        print s
    else:
        new = ""
        for i in a:
            new += str(i)
        print new
            
        
    
            
# true_length()
string_compression()
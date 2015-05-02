def same_letter():
    a = "abca"
    b = "baac"
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if(a == b):
        print "yes"
    else:
        print "no"
        
def same_letter1():
    a = "abcd"
    b = "abbc"
    flag = 1
    hash_map_a = {}
    hash_map_b = {}
    for outer in range(0, len(a)):
        if not(a[outer] in hash_map_a):
            hash_map_a[a[outer]] = 0 
        else:
            hash_map_a[a[outer]] += 1
    for outer in range(0, len(b)):
        if not(b[outer] in hash_map_b):
            hash_map_b[b[outer]] = 0 
        else:
            hash_map_b[b[outer]] += 1
        
    for key, value in dict.items(hash_map_a):
        if key in hash_map_b:
            if hash_map_b[key] != hash_map_a[key]:
                flag = 0
        else:
            flag = 0
    if flag == 1:
        print "true"
    else:
        print "false"

        
def same_letter2():
    a = "abcd"
    b = "cbad"
    flag = 1
    hash_map_a = {}
    hash_map_b = {}
    if len(a) != len(b):
        flag = 0
    for outer in range(0, len(a)):
        if not(a[outer] in hash_map_a):
            hash_map_a[a[outer]] = 1  
        else:
            hash_map_a[a[outer]] += 1
    for outer in range(0, len(b)):
        if not(b[outer] in hash_map_a):
            flag = 0
        else:
            hash_map_a[b[outer]] -= 1
            if hash_map_a[b[outer]] < 0:
                flag = 0
    if flag == 1:
        print "true"
    else:
        print "false"
                
    
    
    
    
same_letter2()
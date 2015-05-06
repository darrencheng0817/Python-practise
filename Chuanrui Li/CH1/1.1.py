#1, brute force + additional string to check the duplicated value
##O(n^2)
def method1():
    flag = 1
    a = "aaaacbbbbbeabaccc"
    b = ""
    for outer in range(0, len(a)):
        inner = outer
        flag =1
        for i in range(inner+1, len(a)):
            if a[i] == a[outer] and flag == 1:
                if a[i] not in b:
                    b = b + a[i]
                    print a[i]
                    flag = 0
                
         
# 1, store the hash key
#     if not find key and insert
#     if find key and insert and updating the value
# 2, iterate the key 
#O(n)
def method2():
    a = "aaaacbbbbbeabaccc"
    hash_map = {}
    for outer in range(0, len(a)):
        if not(a[outer] in hash_map):
            hash_map[a[outer]] = 0 
        else:
            hash_map[a[outer]] += 1
    for key, value in dict.items(hash_map):
        if(value >= 1):
            print key
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

#read the data
data = sys.stdin.readlines()
number = int(data[0])
def helper(line):
    line = line.split()
    line = map(lambda s:int(s), line)
    return line
array = map(helper, data[1:-1])
k = int(data[-1])

#check the duplicates
def calc(number, array, k):
    #loop through all the element in the matrix
    for i in range(number):
        row = array[i]
        l = len(row)
        for j in range(l):
            e = row[j]
            #check the element in the matrix
            for m in range(-k, k+1):
                k2 = k-abs(m)
                for n in range(-k2, k2+1):
                    #skip itself
                    if (m == 0 and n == 0):
                        continue
                    #check within the range
                    if ( i+m >=0 and i+m < number and j+n < len(array[i+m]) and j+n >= 0):
                        e2 = array[i+m][j+n] 
                        if e2 == e:
                            print "YES"
                            return
    print "NO"  
    
calc(number, array, k)
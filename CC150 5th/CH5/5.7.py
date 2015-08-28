#An array A[1...n] contains all the integers from 0 to n except for one number which is missing. In this problem, we cannot access an entire integer in A with a single opera- tion. The elements of A are represented in binary, and the only operation we can use to access them is “fetch the jth bit of A[i]”, which takes constant time. Write code to find the missing integer. Can you do it in O(n) time?

B = [00,01,10,11]
A = [000, 001,  11, 100, 101, 110, 111]
n = 7
def binary_to_int(num):
    #print "--------------"
    #print num
    sum_x = 0
    x = 0
    power = 0
    
    while num != 0:
        x = num % 10
        sum_x  += x * pow(2, power)
        power += 1
        num = num / 10
    return sum_x
    
def sum_value():
    global A
    global n
    real_sum = 0
    for elem in A:
        x =  binary_to_int(elem)
        real_sum += x
    print real_sum
    print n*(n+1)/2 - real_sum
    
sum_value()
        
    
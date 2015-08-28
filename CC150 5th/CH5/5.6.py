#Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc).

#1), we can move odd forward by one and mask the bit for only odd
#2), we can move even backward by one and mask the bit for only even
#3), we combine both forward and backward
# I do not choose to do this cos python do no support this feature (only for int bit wise operation) -> see second approach


def swap_function():
    list1 = []
    num1 = 10110101
    num = 1234
    while num != 0:
        x = num%10
        list1 = [x] + list1
        num = num/10  
    print list1
    for i in range(0, len(list1)-1, 2):
        temp = list1[i]
        list1[i] = list1[i+1]
        list1[i+1] = temp
    print list1

def swap2():
    #111101 -> 111110
    #111010 -> 110101
    num = 58
    num1 = (num >> 1) & 341
    num2 = (num << 1) & 170
    num = num1 | num2
    print num
    
        
swap2()
#Write a function to determine the number of bits required to convert integer A to integer B.

# covert two integer into binary
#check the binary one by one and if there is a dismatch
#----counter increment

#Input: 31, 14 Output: 2

#convert int into binary
def int_to_binary(num):
    power = 0
    x = 0
    sum_x = 0
    while num != 0:
        #binary number x
        x = num % 2 
        sum_x += x * pow(10, power)
        #reminder
        num = num / 2
        power += 1      
    return sum_x

def match(num1, num2):
    counter = 0
    num1 = int_to_binary(num1)
    num2 = int_to_binary(num2)
    print num1, num2
    diff = len(str(num1)) - len(str(num2))
    while num1 != 0 and num2 != 0:
        a = num1 % 10
        b = num2 % 10
        if a != b:
            counter += 1
        num1 = num1/10
        num2 = num2/10
    print counter + diff
    

match(32, 14)
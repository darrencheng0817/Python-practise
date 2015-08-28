#Given a (decimal - e.g. 0.72) number that is passed in as a string, print the 32 bits binary rep- resentation. If the number can not be represented accurately in binary, print “ERROR”

# the number base 5th version, the number is between 0 to 1, the max number is 1 - 2^(-32)

# 1), There are two types of binary representations, first binary cannot represent the double, second binary exceeds the limited of 32 bits

def checking():
    num = 0.375

    #check the max value boundary
    if num > 1 - pow(2, -32):
        return "error"
    power = -1
    bit = 0
    #check 32 bits
    times = 0
    
    while num != 0:
        num = num * 2
        x = int(num)
        bit += pow(10, power) * x
        num = num - x  
        power -= 1
    print bit
        
checking()